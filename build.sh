#!/bin/sh

HOME_DIR=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

docker build -t progin10min/crypto-bert-api .
docker tag progin10min/crypto-bert-api progin10min/crypto-bert-api:latest


