#!/bin/sh

HOME_DIR=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

docker run -d -p 8001:8001 progin10min/crypto-bert-api
