#!/usr/bin/env bash

docker build . -t raydouglass/dreamhost-dynamic-dns:latest
docker push raydouglass/dreamhost-dynamic-dns:latest