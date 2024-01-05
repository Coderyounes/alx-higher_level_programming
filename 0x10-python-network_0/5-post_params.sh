#!/bin/bash
# Bash Script Perform a POST request with a parameters
curl -s -X POST "$1" -d 'email=test%40gmail&subject=I%20will%20always%20be%20here%20for%20PLD'
