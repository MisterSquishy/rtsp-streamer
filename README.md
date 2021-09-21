# birdcam streamer
uses `ffmpeg` to stream rtsp to hls

### build
`docker build -t stream .`

#### run
`docker run -it -p 8080:8080 --restart=always rtsp-stream-python`
