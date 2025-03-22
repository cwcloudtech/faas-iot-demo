#!/usr/bin/env bash

source ./ci/common.sh

sudo apt update -y
sudo apt install -y python3-tk

kill_process "screen"
create_venv
start_process "screen"
exit 0
