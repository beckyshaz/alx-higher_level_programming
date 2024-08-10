#!/bin/bash
# metohods allowed by the server
curl -s -I "$"  | grep "Allow" | cut -d " " -f 2-
