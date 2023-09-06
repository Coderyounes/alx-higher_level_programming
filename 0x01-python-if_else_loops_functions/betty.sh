#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <c_file>"
    exit 1
fi

c_file="$1"

if [ ! -f "$c_file" ]; then
    echo "Error: File not found: $c_file"
    exit 1
fi

# Remove comments using sed
sed -i '/\/\*/,/\*\//d' "$c_file"
sed -i 's/\/\/.*$//' "$c_file"

# Format the code using the 'indent' command
indent -kr -i8 -ts8 -sob -l80 -ss -ncs -npcs -cli8 -c0 "$c_file"

echo "Formatted and comments removed: $c_file"
