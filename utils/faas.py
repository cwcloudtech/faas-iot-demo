  

import requests

from utils.config import get_config, override_conf_from_env
from utils.logger import log_msg

conf = get_config("common")

override_conf_from_env(conf, 'api_url')
override_conf_from_env(conf, 'api_key')
override_conf_from_env(conf, 'function_id')

def parse_response(r):
    payload = {}
    try:
        payload = r.json()
    except:
        payload['raw_body'] = r.content

    if 'status' not in payload:
        payload['status'] = r.status_code >= 200 and r.status_code < 400

    if 'status_code' not in payload:
        payload['status_code'] = r.status_code

    return payload

def call_serverless_function(temperature, humidity):
    url = f"{conf['api_url']}/v1/faas/invocation"

    args = [
        {
            "key": "temperature",
            "value": f"{temperature}"
        },
        {
            "key": "humidity",
            "value": f"{humidity}"
        }
    ]

    headers = {
        "accept": "application/json", 
        "Content-Type": "application/json", 
        "X-Auth-Token" : conf['api_key'] 
    }

    log_msg("INFO", f"headers=${headers}")

    body = {
        "content": {
            "function_id": conf['function_id'],
            "args": args
        }
    }

    r = requests.post(url, headers=headers, json=body)
    payload = parse_response(r)
    log_msg("INFO", f"[faas][call_serverless_function] response = {payload}")
