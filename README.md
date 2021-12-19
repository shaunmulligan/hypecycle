# Hypecycle

An over engineered cycling computer using web tech.

## Todo:

- [ ] Start BLE sensors from registered devices list in DB
- [ ] app.ble.sensor needs to support HRM, Power, Cadence readings
- [ ] app.ble.sensor needs to periodically retry.
- [ ] Add tables for Power, Cadence
- [ ] Add table for location
- [ ] Add table for altitude, temperature, humidity
- [ ] Periodically restart `bluetoothd` to clear cache so CPU doesn't get consumed as per https://github.com/hbldh/bleak/issues/500 maybe just with something like https://newbedev.com/how-can-i-configure-a-systemd-service-to-restart-periodically

## Calculate distance from two lat/long coordinates
https://www.movable-type.co.uk/scripts/latlong.html

## General stack notes:

We installed python 3.10 following this article: https://computingforgeeks.com/how-to-install-python-on-debian-linux/

Installed nodejs 16.x with https://lindevs.com/install-node-js-and-npm-on-raspberry-pi/ 

## Installing hyperpixel:

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

## Launch fastAPI app:
```
cd ~/overkill/backend/src
uvicorn main:app --host 0.0.0.0 --reload
```

## Bluetooth stuff

ble service database https://github.com/NordicSemiconductor/bluetooth-numbers-database 