import json
import sensors_pack.humidity_pack.dht22 as dht22

from time import sleep

from utils.common import is_not_empty, override_conf_from_env, cast_int
from utils.logger import log_msg

with open('sensor.json') as json_file:
    conf = json.load(json_file)

override_conf_from_env(conf, 'log_level')
override_conf_from_env(conf, 'pin')
override_conf_from_env(conf, 'wait_time')

_wait_time = cast_int(conf['wait_time'])
_data_pin = cast_int(conf['pin'])

while True:
    humid, temp = dht22.read_humidity_and_temperature(_data_pin)
    if is_not_empty(humid) and is_not_empty(temp):
        log_msg("INFO", "Temperature={0:0.1f}*C Humidity={1:0.1f}%".format(temp, humid))
    else:
        log_msg("ERROR", "Failed to retrieve values...")

    sleep(_wait_time)
