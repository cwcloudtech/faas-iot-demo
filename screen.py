import json

import paho.mqtt.client as paho
from paho import mqtt

from utils.certs import create_cert_locally
from utils.common import is_empty, is_empty_key, is_true
from utils.config import get_config, override_conf_from_env
from utils.gui import display
from utils.logger import log_msg

conf = get_config("screen")

conf_keys = [
    'gui_close_after',
    'callback_type',
    'callback_url',
    'callback_client_id',
    'callback_user_data',
    'callback_username'
    'callback_password',
    'callback_broker_endpoint',
    'callback_port',
    'callback_subscription'
    'callback_qos'
    'callback_topic'
    'callback_certificates_required',
    'callback_iot_hub_certificate',
    'callback_device_certificate',
    'callback_device_key_certificate'
]

for key in conf_keys:
    override_conf_from_env(conf, key)

def on_connect(client, userdata, flags, rc, properties=None):
    log_msg("DEBUG", "[screen][on_connect] CONNACK received with code %s." % rc)
    client.subscribe(conf['callback_subscription'], qos=int(conf['callback_qos']))

def on_publish(client, userdata, mid, properties=None):
    log_msg("DEBUG", "[screen][on_publish] mid: {}".format(str(mid)))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    log_msg("DEBUG", "[screen][on_subscribe] Subscribed: {} {}".format(str(mid), str(granted_qos)))

def on_message(client, userdata, msg):
    log_msg("DEBUG", "[screen][on_message] topic: {} qos: {} payload: {}".format(msg.topic, str(msg.qos), str(msg.payload)))
    payload = json.loads(msg.payload.decode("UTF-8"))
    if is_empty_key(payload, 'content'):
        log_msg("ERROR", f"[screen][on_message] invalid payload: {payload}")
        return

    if payload['content']['state'] == "complete":
        display(conf, "I feel", payload['content']['result'])

client = None
if conf['callback_type'] == "mqtt":
    log_msg("INFO", "[screen] invoke mqtt callback: {}".format(conf['callback_url']))
    client = paho.Client(client_id=conf['callback_client_id'], userdata=conf['callback_user_data'], protocol=paho.MQTTv5)
elif conf['callback_type'] == "websocket":
    log_msg("INFO", "[screen] invoke websocket callback: {}".format(conf['callback_url']))
    client = paho.Client(client_id=conf['callback_client_id'], userdata=conf['callback_user_data'], transport='websockets')

if is_empty(client):
    log_msg("ERROR", "[screen] unable to create client, check your configuration")
    exit(1)

client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

if is_true(conf['callback_certificates_required']):
    create_cert_locally("iot_hub_certificate", conf['callback_iot_hub_certificate'])
    create_cert_locally("device_certificate", conf['callback_device_certificate'])
    create_cert_locally("device_key_certificate", conf['callback_device_key_certificate'])
    client.tls_set(
        ca_certs="./iot_hub_certificate.pem",
        certfile="./device_certificate.pem",
        keyfile="./device_key_certificate.pem",
        tls_version=mqtt.client.ssl.PROTOCOL_TLS
    )
else:
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

client.username_pw_set(conf['callback_username'], conf['callback_password'])
client.connect(conf['callback_url'], conf['callback_port'])

client.loop_forever()
