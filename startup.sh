#!/bin/sh

INPUT=$PARAMETERS

COUNTER=0
IN=""
OUT=""
for parameter in $INPUT
do
    if [ $COUNTER -eq 0 ]; then
      IN=$parameter
    fi
    if [ $COUNTER -eq 1 ]; then
      OUT=$parameter
      echo "Starting ${OUT} stream"
      $(sh ./create_ffmpeg_cmd.sh ${IN} ${OUT}) &
      COUNTER=0
      IN=""
      OUT=""
      continue
    fi
    COUNTER=$((COUNTER+1))
done

trap on_sigint SIGINT
on_sigint() { echo "goodbye"; }

nginx -g "daemon off;"
