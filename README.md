# videoTools
simple python program that uses FFMPEG to compress video files.

## Dependencies

```bash
pip3 install -U ffmpeg ffmpeg-python termcolor
```

## How to use

### Help Message

```bash
python3 ./main.py --help
```

And the output will be:

```text
usage: main.py [-h] [-p PATH] [-o OUTPUT] [-b BITRATE] [-c CRF] [-d DIRECTORY]

optional arguments:
  -h, --help            show this help message and exit

  -p PATH, --path PATH  Video path.

  -o OUTPUT, --output OUTPUT
                        Where to save file. (Directroy)

  -b BITRATE, --bitrate BITRATE
                        Target video bitrate.

  -c CRF, --crf CRF     Target video crf.

  -d DIRECTORY, --directory DIRECTORY
```

- **Only use one of `-c` or `-b` options**

- **`-d` option will give a directory as input and searches that recursively to find `.mp4`, `.mkv` and `.avi` file to compress**

