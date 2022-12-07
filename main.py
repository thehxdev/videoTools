#!/usr/bin/env python3

import argparse
import ffmpeg
import sys
import os
import termcolor
import glob
import re

parser = argparse.ArgumentParser()

parser.add_argument(
    '-p',
    '--path',
    help = 'Video path.',
)

parser.add_argument(
    '-o',
    '--output',
    help = 'Where to save file. (Directroy)',
)

parser.add_argument(
    '-b',
    '--bitrate',
    help = 'Target video bitrate.',
    type = int,
)

parser.add_argument(
    '-c',
    '--crf',
    help = 'Target video crf (0 - 50). Lower has better Quality and LESS compression.',
    type = int,
)

parser.add_argument(
    '-d',
    '--directory',
    help = 'Videos from a directory.',
)

class PrintStatus:

    @staticmethod
    def ok(msg:str) -> None:
        msg = termcolor.colored(f'[OK] {msg}', 'green')
        print(msg)

    @staticmethod
    def info(msg:str) -> None:
        msg = termcolor.colored(f'[ERROR] {msg}', 'red')
        print(msg)

    @staticmethod
    def error(msg:str) -> None:
        msg = termcolor.colored(f'[INFO] {msg}', 'yellow')
        print(msg)


class Video:
    
    def __init__(self,
                 videoPath:str,
                 outputPath:str,
                 bitrateOrCrf_Num: int,
                 compressMethod:str = 'bitrate',
                 ):
        self.videoPath      = videoPath
        self.outputPath     = outputPath
        self.videoName      = os.path.splitext(self.videoPath)[0].split('/')[-1]
        self.videoExtention = os.path.splitext(self.videoPath)[1]
        self.outputSuffix   = '_cmp'
        self.output_file    = self.outputPath + self.videoName + self.outputSuffix + self.videoExtention
        self.compressMethod = compressMethod
        self.bitrateOrCrf_Num   = bitrateOrCrf_Num

    def compress(self):
        inputVid = ffmpeg.input(self.videoPath)
        if self.compressMethod == 'bitrate':
            ffmpeg.output(
                inputVid,
                self.output_file,
                **{'c:v': 'libx264', 'b:v': f'{self.bitrateOrCrf_Num}k', 'preset': 'veryfast'}
            ).overwrite_output().run()
        elif self.compressMethod == 'crf':
            ffmpeg.output(
                inputVid,
                self.output_file,
                **{'c:v': 'libx264', 'crf': self.bitrateOrCrf_Num, 'preset': 'veryfast'}
            ).overwrite_output().run()


        PrintStatus.ok('Video Compressed!')

    def getInfo(self):
        pass

    def play(self):
        pass

def runCompressor(vidPath:str):
    if args.bitrate:
        vid = Video(vidPath, args.output, args.bitrate, compressMethod='bitrate')
        try:
            vid.compress()
        except KeyboardInterrupt:
            sys.exit()
    elif args.crf:
        vid = Video(vidPath, args.output, args.crf, compressMethod='crf')
        try:
            vid.compress()
        except KeyboardInterrupt:
            sys.exit()


if __name__ == '__main__':
    args = parser.parse_args()

    if args.directory:
        valid_formats = ['.mp4', '.mkv', '.avi']
        files = []
        for filename in glob.iglob(args.directory + '**/**', recursive=True):
            if os.path.splitext(filename)[1] in valid_formats:
                if re.search('_cmp.[mp4,mkv,avi]', filename):
                    continue
                runCompressor(filename)
    else:
        runCompressor(args.path)

