#!/bin/bash
# Bash Script Perform a POST request with a parameters in JSON
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
