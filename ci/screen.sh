#!/usr/bin/env bash

source ./ci/common.sh

kill_process "screen"
create_venv
start_process "screen" "cwcloud"
exit 0
