#!/usr/bin/env bash

export VENV_PATH="./vdemo"

create_venv() {
    if [[ ! -d $VENV_PATH ]]; then
        python3 -m venv $VENV_PATH
        echo "export PYTHONDONTWRITEBYTECODE=1" >> $VENV_PATH/bin/activate
        echo "export CWCLOUD_DEMO_api_key=${CWCLOUD_DEMO_api_key}" >> $VENV_PATH/bin/activate
        $VENV_PATH/bin/pip install --upgrade pip setuptools wheel
    fi
}
