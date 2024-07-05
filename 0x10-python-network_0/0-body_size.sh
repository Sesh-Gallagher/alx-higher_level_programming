#!/bin/bash
# script that takes in a URL, sends a request to that URL, and display it
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
