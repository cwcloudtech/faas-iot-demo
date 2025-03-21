#!/usr/bin/env bash

venv_path="./vdemo"

create_venv() {
    if [[ ! -d $venv_path ]]; then
        python3 -m venv $venv_path
        echo "export PYTHONDONTWRITEBYTECODE=1" >> $venv_path/bin/activate
        echo "export CWCLOUD_DEMO_api_key=${CWCLOUD_DEMO_api_key}" >> $venv_path/bin/activate
    fi
}

kill_sensor() {
    ps -ef|awk '($0 ~ "sensor.py" && $0 ~ "python" && $0 !~ "awk"){system ("kill -9 "$2" ; kill -9 "$3)}'
}

start_sensor() {
    $venv_path/bin/pip install --upgrade pip setuptools wheel
    $venv_path/vdemo/bin/pip install -r sensor.requirements
    sudo echo "${CWCLOUD_DEMO_api_key}" > /root/api_key.txt
    sudo ./vdemo/bin/python sensor.py & disown
}

kill_sensor
create_venv
start_sensor & disown
exit 0
