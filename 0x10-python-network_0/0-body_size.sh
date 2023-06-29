#!/bin/bash
# script to display response size for URL passed to script
curl -s "$1" | wc -c
