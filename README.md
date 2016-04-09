zumopi
=================
Use a Wiimote and explorer pHAT to control your Polulu Zumo Robot!

![Zumo robot from the side](https://raw.githubusercontent.com/alexellis/zumopi/master/media/zumo.jpg)


### Hardware

Basics:

* Raspberry PI (i.e. the PI Zero)
* pHAT explorerhat from Pimoroni
* Bluetooth USB dongle (£1 type is OK)
* Wiimote

Robot-parts:

* Zumo robot kit from Pimoroni
* 2x 1:50 micro metal gear-motors
* 1x 3A Hobbywing UBEC 5v
* 4x Jumper cables

#### Connections

Solder the UBEC's input wires (red/black) to the AA battery terminals.

Connect the UBEC's output wires to the 5v/GND on the explorerhat. This will now supply 5v to the PI itself.

Take your 4x jumper cables and cut off one end of each wire, then solder the wires to the micro metal gear-motors.

Connect the male end of your jumper cables into Motors [1 +/- and 2 +/-]


### Installation

#### For installing on Raspbian:

Clone the repo:

```
cd /home/pi/
git clone https://github.com/alexellis/zumopi.git
```

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
