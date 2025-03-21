#!/usr/bin/env bash

source ./ci/common.sh

kill_sensor() {
    ps -ef|awk '($0 ~ "sensor.py" && $0 ~ "python" && $0 !~ "awk"){system ("sudo kill -9 "$2" ; sudo kill -9 "$3)}'
}

start_sensor() {
    $VENV_PATH/bin/pip install -r sensor.requirements
    sudo $VENV_PATH/python sensor.py
}

kill_sensor
create_venv
start_sensor & disown
exit 0
