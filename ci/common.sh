#!/usr/bin/env bash

export VENV_PATH="./vdemo"

create_venv() {
    if [[ ! -d $VENV_PATH ]]; then
        python3 -m venv $VENV_PATH
        echo "export PYTHONDONTWRITEBYTECODE=1" >> $VENV_PATH/bin/activate
        echo "export TK_SILENCE_DEPRECATION=1" >> $VENV_PATH/bin/activate
        echo "export CWCLOUD_DEMO_api_key=${CWCLOUD_DEMO_api_key}" >> $VENV_PATH/bin/activate
        $VENV_PATH/bin/activate
        $VENV_PATH/bin/pip install --upgrade pip setuptools wheel
    fi
}

kill_process() {
    ps -ef|awk '($0 ~ "'"${1}"'.py" && $0 ~ "python" && $0 !~ "awk"){system ("kill -9 "$2)}'
}

start_process() {
    $VENV_PATH/bin/activate
    $VENV_PATH/bin/pip install -r "${1}.requirements"
    $VENV_PATH/bin/python "${1}.py" &> "${1}.log" & disown -h
    sleep 2
    cat "${1}.log"
}
