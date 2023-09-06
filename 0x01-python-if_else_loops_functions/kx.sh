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

# Remove // comments using sed
sed -i '/\/\//d' "$c_file"

# Format the code using the 'indent' command
indent -kr -i8 -ts8 -sob -l80 -ss -ncs -npcs -cli8 -c0 "$c_file"

# Handle specific cases
sed -i 's/\(.*\)\*\s\+\(.*\)/\1*\2/' "$c_file" # Fix "foo * bar" to "foo *bar"
sed -i '/^\s*}\s*$/d' "$c_file"                # Remove blank lines with only '}' characters
sed -i '/^[ \t]*{/d' "$c_file"                # Remove open braces '{' following function declarations on the same line
sed -i 's/\(.*\)\S\+;/\1;/' "$c_file"         # Add a space before semicolon at the end of lines

echo "Formatted with specific cases handled: $c_file"

