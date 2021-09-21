FROM python:3.7-buster

RUN mkdir /tmp/stream
RUN apt update
RUN apt install ffmpeg -y

COPY . /
RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "main.py"]
