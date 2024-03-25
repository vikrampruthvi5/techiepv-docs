#!/bin/bash

cd /Users/pvikram/Documents/docs
ls -altr
sphinx-build -M html source build
aws s3 cp ./build/html/ s3://techiepv.com --recursive
