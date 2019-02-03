#!/bin/bash
docker build -t test_build:latest .
docker run --rm -d -p 5000:5000 test_build
