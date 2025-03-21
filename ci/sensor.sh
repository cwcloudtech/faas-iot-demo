#!/usr/bin/env bash

venv_path="./vdemo"

ps -ef|awk '($0 ~ "sensor.py" && $0 ~ "python" && $0 !~ "awk"){system ("kill -9 "$2)}'
[[ -d $venv_path ]] || python3 -m venv ./vdemo

export PYTHONDONTWRITEBYTECODE=1

./vdemo/bin/pip install --upgrade pip setuptools wheel
./vdemo/bin/pip install -r requirements.txt
sudo ./vdemo/bin/python sensor.py & disown
exit 0
