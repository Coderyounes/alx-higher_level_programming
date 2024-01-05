#!/bin/bash
# Bash Script Perform a GET with a Customized Header
curl -s -X GET "$1" -H "X-School-User-Id: 98"