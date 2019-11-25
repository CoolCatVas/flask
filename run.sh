#!/bin/sh

gunicorn application:app -b 127.0.0.1:$PORT -w=4