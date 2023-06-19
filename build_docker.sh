#!/usr/bin/env bash

docker build . -t raydouglass/dreamhost-dynamicdns:latest
docker push raydouglass/dreamhost-dynamicdns:latest