#!/usr/bin/env bash

source ./ci/common.sh

kill_process "screen"
create_venv
sudo -u cwcloud start_process "screen"
exit 0
