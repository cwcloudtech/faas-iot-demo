import adafruit_dht
import board

from time import sleep

from utils.common import cast_int
from utils.config import get_config, override_conf_from_env
from utils.logger import log_msg

conf = get_config("sensor")

override_conf_from_env(conf, 'log_level')
override_conf_from_env(conf, 'pin')
override_conf_from_env(conf, 'wait_time')

_wait_time = cast_int(conf['wait_time'])
_pin = conf['pin']
gpio_pin = getattr(board, f"D{_pin}")

_sensor = adafruit_dht.DHT22(gpio_pin)

while True:
    temp = _sensor.temperature
    humidity = _sensor.humidity

    log_msg("INFO", f"Temperature={temp} Humidity={humidity}")
    sleep(_wait_time)
