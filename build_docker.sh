#!/usr/bin/env bash

docker buildx build \
    --platform=linux/amd64,linux/arm64,linux/ppc64le,linux/s390x,linux/arm/v7,linux/arm/v6 \
    -t raydouglass/dreamhost-dynamic-dns:latest \
    --push \
    .
