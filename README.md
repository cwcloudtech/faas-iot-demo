# FaaS IoT Demo cwcloud

## Requirements

### Hardware

You need a RaspberryPi 4 model B with 4GB ram or more:

![rpi4](./img/rpi4.png)

And a DHT22 temperature and humidity sensor wired as described below:

![gpio](./img/gpio.png)

* `+` plugged in pin 1 (`3.3V`)
* `out` plugged in pin 11 (`#17`)
* `-` plugged in pin 9 (`GND`)

### Software

Packages to install

```shell
sudo apt update -y
sudo apt dist-upgrade -y
sudo apt autoremove -y
sudo apt install -y git build-essential fonts-noto-color-emoji python3-tk x11-apps
```

If you want to use the [gitlab CI pipeline](./.gitlab-ci.yml), also install gitlab runner:

```shell
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash
sudo apt -y install gitlab-runner
gitlab-runner register
```

## Run and update the code manually

### Run the sensor code

1. Change the values containing `changeit` value in the configurations json files: [common.json](./common.json) and [sensor.json](./sensor.json)
2. Run the following commands:

```shell
python3 -m venv ./vdemo
source ./vdemo/bin/activate
./vdemo/bin/pip install --upgrade pip setuptools wheel
./vdemo/bin/pip install -r sensor.requirements
./vdemo/bin/python sensor.py
```

### Run the screen code

```shell
python3 -m venv ./vdemo
source ./vdemo/bin/activate
./vdemo/bin/pip install --upgrade pip setuptools wheel
./vdemo/bin/pip install -r screen.requirements
./vdemo/bin/python screen.py
```
