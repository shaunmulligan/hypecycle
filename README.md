# Hypecycle

An over engineered cycling computer using web tech. The plan is to create a semi-useable, battery powered cycling computer. The goal is not to make the ultimate cycle computer, but rather to learn new technologies and build something that is useful and fun.

### Hardware
- Raspberry Pi Zero 2 W
- Hyperpixel 4.0 LCD
- Adafruit Mini GPS PA1010D
- Adafruit Blinka MCP2221 for i2c, button, adc
- PowerBoost 1000 LiPo Charger 5V 1A Boost and LiPo Battery
- RPi mini camera (not yet working on debian bullseye)
- ICP-10125 Air Pressure Sensor Breakout (High Accuracy Pressure / Altitude)

### Software
Using the following technologies:
- Python3 + FastAPI for the backend
- svelte.js + ionic framework for the frontend
- balena cloud for easy deployment (later maybe)

### Feature Set
- Base Features:
    - Bluetooth LE sensor support
        - 4iii: speed, cadence, and power
        - Garmin HRM: Heart rate
    - GPS tracking
        - Lat, Lon
        - Altitude
        - Speed
        - Direction
        - Temperature
        - Quick TTFF using assisted GPS (see https://github.com/gtjoseph/mt3339-utils )
    - Save ride to GPX file
    - Upload ride to Garmin Connect or Strava when connected to wifi.
    - Offline Maps with route and elevation data
    - Front facing LED lighting (neopixel??)
- Stretch Goals:
    - ANT+ support 
        - 4iii: speed, cadence, and power
        - Garmin HRM: Heart rate
    - Orientation via BNO055
        - Pitch, Roll, Yaw
        - acceleration, gyro, and magnetometer
        - temperature

## Todo:

- [ ] Start BLE sensors from registered devices list in DB
- [ ] app.ble.sensor needs to support HRM, Power, Cadence readings
- [ ] app.ble.sensor needs to periodically retry.
- [ ] Add tables for Power, Cadence
- [ ] Add table for location
- [ ] Add table for altitude, temperature, humidity
- [ ] Periodically restart `bluetoothd` to clear cache so CPU doesn't get consumed as per https://github.com/hbldh/bleak/issues/500 maybe just with something like https://newbedev.com/how-can-i-configure-a-systemd-service-to-restart-periodically

## Usage
To launch chrome pointing at frontend server:
```
DISPLAY=:0 chromium-browser --kiosk http://192.168.86.38:5000
```
To start frontend server:
```
cd fronend && npm start
```
To start backend server:
```
bash launch.sh
```

## Calculate distance from two lat/long coordinates
https://www.movable-type.co.uk/scripts/latlong.html

### Switch off LCD backlight:
```
echo 1 |sudo tee /sys/class/backlight/rpi_backlight/bl_power
```

### dim LCD screen
```
import pigpio
gpio = pigpio.pi()
gpio.set_PWM_dutycycle(19, 64)  #0-255, so 64 is 1/4 duty cycle
```
Be sure to run sudo pigpiod to start the daemon before you run this script.

## Bluetooth stuff

ble service database https://github.com/NordicSemiconductor/bluetooth-numbers-database 

### Useful Links:
- Develop with QWIIC modules on macOS: https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221 
- Mapping:
    - Offline leaflet maps https://github.com/allartk/leaflet.offline 
    - GPX layered on to Leaflet map: https://github.com/mpetazzoni/leaflet-gpx 
- BLE:
    - https://github.com/zacharyedwardbull/pycycling
- ANT:
    - https://github.com/Tigge/openant

## Install

### General stack notes:

We installed python 3.10 following this article: https://computingforgeeks.com/how-to-install-python-on-debian-linux/

Installed nodejs 16.x with https://lindevs.com/install-node-js-and-npm-on-raspberry-pi/ 

### Installing hyperpixel:

First need to run the below to get around apt issues:
```
sudo apt-get --allow-releaseinfo-change update

```
then install the actual lib, following prompts:
```
curl https://get.pimoroni.com/hyperpixel4 | bash
```
After that is complete and device is rebooted, we can symlink the i2c-3 so that we don't have to change our i2c bus code using:
```
sudo ln -s /dev/i2c-3 /dev/i2c-1
```
Set orientation of screen:
```
hyperpixel4-rotate normal
```

### Install adafruit blinka support:
```
sudo pip install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python raspi-blinka.py
```

install usb MCP2221 support:
```
sudo apt-get install libusb-1.0 libudev-dev
```

## Assisted GPS:

need to load an EPO file 

look at https://github.com/gtjoseph/mt3339-utils 

## Prior Art
- pizero_bikecomputer: https://github.com/hishizuka/pizero_bikecomputer

