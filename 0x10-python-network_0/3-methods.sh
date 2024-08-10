#!/bin/bash
# metohods allowed by the server
curl -s -I "1$" | grep "Allow" | cut -d " " -f 2-
