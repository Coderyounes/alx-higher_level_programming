#!/bin/bash
# Bash Script display The Status Code
curl -s "$1" -w "%{http_code}" -o /dev/null
