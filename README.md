# birdcam streamer
uses `ffmpeg` to stream rtsp to hls

### build
`docker build -t stream .`

#### run
`docker run -it -p 8080:8080 --restart=on-failure -e INPUT=rtsp://peteybirds:Birdz123@192.168.1.16/live -e OUTPUT=birdcam -v /tmp/stream:/tmp/stream stream`
