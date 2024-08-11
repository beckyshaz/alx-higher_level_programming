#!/bin/bash
# Requesting for status code
curl -sw "%{http_code}" -o /dev/null "$1"
