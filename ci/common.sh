#!/usr/bin/env bash

export VENV_PATH="./vdemo"

create_venv() {
    if [[ ! -d $VENV_PATH ]]; then
        python3 -m venv $VENV_PATH
        echo "export PYTHONDONTWRITEBYTECODE=1" >> $VENV_PATH/bin/activate
        echo "export TK_SILENCE_DEPRECATION=1" >> $VENV_PATH/bin/activate
        echo "export DISPLAY=:0.0"
        echo "export CWCLOUD_DEMO_api_key=\"${CWCLOUD_DEMO_api_key}\"" >> $VENV_PATH/bin/activate
        echo "export CWCLOUD_DEMO_callback_url=\"${CWCLOUD_DEMO_callback_url}\"" >> $VENV_PATH/bin/activate
        echo "export CWCLOUD_DEMO_callback_username=\"${CWCLOUD_DEMO_callback_username}\"" >> $VENV_PATH/bin/activate
        echo "export CWCLOUD_DEMO_callback_password=\"${CWCLOUD_DEMO_callback_password}\"" >> $VENV_PATH/bin/activate
        source $VENV_PATH/bin/activate
        $VENV_PATH/bin/pip install --upgrade pip setuptools wheel
    fi
}

kill_process() {
    ps -ef|awk '($0 ~ "'"${1}"'.py" && $0 ~ "python" && $0 !~ "awk"){system ("kill -9 "$2)}'
}

start_process() {
    source $VENV_PATH/bin/activate
    $VENV_PATH/bin/pip install -r "${1}.requirements"
    $VENV_PATH/bin/python "${1}.py" &> "${1}.log" & disown -h
    sleep 2
    cat "${1}.log"
}
