# FaaS IoT Demo cwcloud

## On the sensor pi

1. Change the `changeit` value in the [sensor.json](./sensor.json) file
2. Run the following commands:

```shell
python3 -m venv ./vdemo
./vdemo/bin/pip install -r requirements.txt --install-option="--force-pi"
./vdemo/bin/python sensor.py
```
