#!/usr/bin/env bash

source ./ci/common.sh

kill_process "sensor"
create_venv
start_process "sensor" & disown $!
exit 0
