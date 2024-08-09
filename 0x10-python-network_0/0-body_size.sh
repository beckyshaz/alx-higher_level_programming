#!/bin/bash
# Getting size of response body
curl -X GET -s -w "%{size_download}\n" -o /dev/null $1
