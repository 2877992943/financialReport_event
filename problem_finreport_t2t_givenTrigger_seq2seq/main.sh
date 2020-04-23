#!/bin/bash


image=tensorflow/tensorflow:1.15.2-gpu-py3

docker run -it --name cc --runtime=nvidia -v /home/op/congc/:/vproblem $image bash