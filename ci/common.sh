#!/usr/bin/env bash

export VENV_PATH="./vdemo"

create_venv() {
    if [[ ! -d $VENV_PATH ]]; then
        python3 -m venv $VENV_PATH
        echo "export PYTHONDONTWRITEBYTECODE=1" >> $VENV_PATH/bin/activate
        echo "export TK_SILENCE_DEPRECATION=1" >> $VENV_PATH/bin/activate
        echo "export DISPLAY=:0.0"

        declare -a vars
        vars=(
            "CWCLOUD_DEMO_api_key"
            "CWCLOUD_DEMO_callback_url"
            "CWCLOUD_DEMO_callback_username"
            "CWCLOUD_DEMO_callback_password"
        )

        declare -a confs
        confs=("common" "sensor" "screen" "demo-faas-iot")

        for var in ${vars[@]}; do
            val="$(printenv $var)"
            for conf in ${confs[@]}; do
                sed -i "s/${var}_changeit/${val}/g" "${conf}.json"
            done
            echo "export ${var}=\"${val}\"" >> $VENV_PATH/bin/activate
        done

        source $VENV_PATH/bin/activate
        $VENV_PATH/bin/pip install --upgrade pip setuptools wheel
    fi
}

kill_process() {
    ps -ef|awk '($0 ~ "'"${1}"'.py" && $0 ~ "python" && $0 !~ "awk"){system ("kill -9 "$2)}'
    rm -rf "${1}.log"
}

start_process() {
    source $VENV_PATH/bin/activate
    $VENV_PATH/bin/pip install -r "${1}.requirements"
    if [[ $2 ]]; then
        sudo -u "${2}" $VENV_PATH/bin/python "${1}.py" &> "${1}.log" & disown -h
    else
        $VENV_PATH/bin/python "${1}.py" &> "${1}.log" & disown -h
    fi
    sleep 2
    cat "${1}.log"
}
