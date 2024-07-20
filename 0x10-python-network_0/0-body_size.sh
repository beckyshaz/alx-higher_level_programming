#!/bin/bash
# Getting size of response body
curl -s -w "%{size_download}\n" $1
