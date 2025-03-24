#!/usr/bin/env bash

source ./ci/common.sh

xhost +localhost
kill_process "screen"
create_venv
start_process "screen"
exit 0
