#!/bin/bash
docker build -t test_build:latest .
docker run -p 5000:5000 test_build
