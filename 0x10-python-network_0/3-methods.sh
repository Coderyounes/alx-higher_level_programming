#!/bin/bash
# Bash Script display Allowed HTTP Methods
curl -s -I "$1" | awk '/^Allow:/ {sub(/^Allow: /, ""); print}'
