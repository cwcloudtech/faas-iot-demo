import os
import json

from utils.common import is_empty, is_empty_key, is_not_empty

_prefix = "CWCLOUD_DEMO"

def get_config(name):
    common = {}
    conf = {}

    with open("common.json") as json_file:
        common = json.load(json_file)

    if name != "common":
        with open(f"{name}.json") as json_file:
            conf = json.load(json_file)

    return {**common, **conf}

def override_conf_from_env(conf, key, default_value = None):
    env_key = f"{_prefix}_{key}"
    if is_not_empty(os.environ.get(env_key)):
        conf[key] = os.environ[env_key]
    elif is_empty_key(conf, key):
        conf[key] = default_value
