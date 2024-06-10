#!/bin/bash

image_path=$1
output_dir=$2

cd ./ultralytics

python detect.py \
    --image $image_path \
    --output $output_dir

