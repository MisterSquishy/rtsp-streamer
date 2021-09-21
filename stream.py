from ffmpeg import FFmpeg

ffmpeg = FFmpeg().option('y').input(
  'rtsp://peteybirds:Birdz123@192.168.1.16/live',
  rtsp_transport='tcp',
  rtsp_flags='prefer_tcp',    
).output(
  '/tmp/stream/birdcam.m3u8',
  {'codec:v': 'copy'},
  f='mpegts',
  hls_list_size=100,
  hls_init_time=1,
  hls_time=1,
  hls_flags='delete_segments'
)

@ffmpeg.on('start')
def on_start(arguments):
  print('Arguments:', arguments)

@ffmpeg.on('stderr')
def on_stderr(line):
  print('stderr:', line)

@ffmpeg.on('progress')
def on_progress(progress):
  print(progress)

@ffmpeg.on('completed')
def on_completed():
  print('Completed')
  exit(1)

@ffmpeg.on('terminated')
def on_terminated():
  print('Terminated')
  exit(1)

@ffmpeg.on('error')
def on_error(code):
  print('Error:', code)