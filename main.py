import asyncio
from threading import Thread
from stream import ffmpeg
from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/<path:name>")
def serve_stream(name):
  return send_from_directory("/tmp/stream/", name)

if __name__ == "__main__":
  T = Thread(target = lambda: app.run('0.0.0.0', 8080))
  T.start()

  loop = asyncio.get_event_loop()
  loop.create_task(ffmpeg.execute())
  loop.run_forever()
