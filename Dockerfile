FROM python:alpine
WORKDIR /videoTools

RUN apk update && apk add ffmpeg

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENTRYPOINT ["python", "./main.py"]
