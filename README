zumopi
=================
Zumo robot control code for Raspberry PI and Wiimote

### Hardware

* Raspberry PI (i.e. the PI Zero)
* pHAT explorerhat from pimoroni
* Bluetooth USB dongle (£1 type is OK)
* zumo robot kit
* 2x 1:50 micro metal gear-motors
* 1x 3A Hobbywing UBEC 5v
* 4x jumper cables
* wiimote

#### Connections

Solder the UBEC's input wires (red/black) to the AA battery terminals.

Connect the UBEC's output wires to the 5v/GND on the explorerhat. This will now supply 5v to the PI itself.

Take your 4x jumper cables and cut off one end of each wire, then solder the wires to the micro metal gear-motors.

Connect the male end of your jumper cables into Motors [1 +/- and 2 +/-]


### Installation

#### For installing on Raspbian:

```
apt-get install bluez
```

Install explorerhat

```
curl get.pimoroni.com/explorerhat | bash
```

#### Start-up command

Because the PI Zero has one USB port we need to start our software automatically.

```
systemctl enable cron
crontab -e
```

Enter this:

```
@reboot /home/pi/zumopi/start.sh
```
