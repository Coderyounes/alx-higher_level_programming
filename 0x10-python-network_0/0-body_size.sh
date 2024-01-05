#!/bin/bash
# Bash Script display the reponse size in byte
curl -sI "$1" | grep 'Content-Length' | sed 's/^Content-Length: //'