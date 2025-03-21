import adafruit_dht
import board

from time import sleep

from utils.common import cast_int, is_true
from utils.config import get_config, override_conf_from_env
from utils.faas import call_serverless_function
from utils.logger import log_msg

conf = get_config("sensor")

override_conf_from_env(conf, 'log_level')
override_conf_from_env(conf, 'pin')
override_conf_from_env(conf, 'wait_time')
override_conf_from_env(conf, 'use_pulseio')

_wait_time = cast_int(conf['wait_time'])
_pin = conf['pin']
gpio_pin = getattr(board, f"D{_pin}")

_sensor = adafruit_dht.DHT22(gpio_pin, is_true(conf['use_pulseio']))

while True:
    try:
        temp = _sensor.temperature
        humidity = _sensor.humidity
    except RuntimeError as e:
        log_msg("ERROR", f"Unexpected error type={type(e)}, error={e}")
        continue

    log_msg("INFO", f"Temperature={temp} Humidity={humidity}")
    call_serverless_function(temp, humidity)
    sleep(_wait_time)
