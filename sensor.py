import json

from time import sleep
from pigpio_dht import DHT22

from utils.common import is_empty_key, is_not_empty, override_conf_from_env, cast_int
from utils.logger import log_msg

with open('sensor.json') as json_file:
    conf = json.load(json_file)

override_conf_from_env(conf, 'log_level')
override_conf_from_env(conf, 'pin')
override_conf_from_env(conf, 'wait_time')

_wait_time = cast_int(conf['wait_time'])
_data_pin = cast_int(conf['pin'])

sensor = DHT22(_data_pin)

while True:
    data = sensor.read()
    if is_empty_key(data, 'temp_c') or is_empty_key(data, 'humidity'):
        log_msg("ERROR", f"Error reading values: data={data}")
        continue

    log_msg("INFO", f"Temperature={data['temp_c']} Humidity={data['humidity']}")
