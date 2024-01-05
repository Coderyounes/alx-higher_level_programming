#!/usr/bin/env bash

if [ -z "$1" ]; then
    echo "USAGE: $0 <URL>"
    exit 1
fi

url="$1"

reponse=$(curl -s -w "%{size_download}" "$url" -o /dev/null)
echo "$reponse"