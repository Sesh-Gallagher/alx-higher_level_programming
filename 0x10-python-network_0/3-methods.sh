#!/bin/bash
# script that takes in a URL and displays HTTP methods the server will accept.
curl -sI "$1" | grep "Allow:" | cut -d ':' -f 2- | cut -c 2-
