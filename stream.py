from ffmpeg import FFmpeg
import os

ffmpeg = FFmpeg().input(
  os.getenv("INPUT"),
  rtsp_transport='tcp',
).output(
  f'/tmp/stream/{os.getenv("OUTPUT")}.m3u8',
  vcodec='h264',
  hls_list_size=100,
  hls_init_time=1,
  hls_time=1,
  hls_flags='delete_segments'
).option('an')

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
