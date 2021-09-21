FROM python:3.7-alpine

RUN apk add --update ffmpeg && rm -rf /var/cache/apk/* && mkdir /tmp/stream

COPY . /
RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "main.py"]
