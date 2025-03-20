from time import sleep
from pigpio_dht import DHT22

from utils.common import is_empty_key, cast_int
from utils.config import get_config, override_conf_from_env
from utils.logger import log_msg
from utils.pigpiod import start_pigpiod

conf = get_config("sensor")

override_conf_from_env(conf, 'log_level')
override_conf_from_env(conf, 'pin')
override_conf_from_env(conf, 'wait_time')

_wait_time = cast_int(conf['wait_time'])
_data_pin = cast_int(conf['pin'])
_retries = cast_int(conf['retries'])
_timeout = cast_int(conf['timeout'])

start_pigpiod()
sensor = DHT22(_data_pin, timeout_secs=_timeout)

while True:
    data = sensor.read(retries=_retries)
    if is_empty_key(data, 'temp_c') or is_empty_key(data, 'humidity'):
        log_msg("ERROR", f"Error reading values: data={data}")
        continue

    log_msg("INFO", f"Temperature={data['temp_c']} Humidity={data['humidity']}")
    sleep(_wait_time)
