# FaaS IoT Demo cwcloud

## Requirements

On both rapberrypi:

```shell
sudo apt update -y
sudo apt dist-upgrade -y
sudo apt autoremove -y
sudo apt install -y git build-essential fonts-noto-color-emoji
```

Install also gitlab runner:

```shell
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash
sudo apt -y install gitlab-runner
gitlab-runner register
```

## On the sensor pi

### Wiring of the Sensor PI

![gpio](./img/gpio.png)

* `+` plugged in pin 1 (`3.3V`)
* `out` plugged in pin 11 (`#17`)
* `-` plugged in pin 9 (`GND`)

### Run and update the code

1. Change the `changeit` value in the [common.json](./common.json) file
2. Run the following commands:

```shell
python3 -m venv ./vdemo
./vdemo/bin/pip install --upgrade pip setuptools wheel
./vdemo/bin/pip install -r sensor.requirements
./vdemo/bin/python sensor.py
```

## On the screen pi

### First install

```shell
sudo apt install -y python3-tk x11-apps
```

### Run and update the code

```shell
python3 -m venv ./vdemo
./vdemo/bin/pip install --upgrade pip setuptools wheel
./vdemo/bin/pip install -r screen.requirements
./vdemo/bin/python screen.py
```
