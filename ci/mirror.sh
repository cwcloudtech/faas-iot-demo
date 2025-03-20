#!/bin/bash

REPO_PATH="${PROJECT_HOME}/faas-iot-demo/"

cd "${REPO_PATH}" && git pull origin main || :
git push github main -f
exit 0
