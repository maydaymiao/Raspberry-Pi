欢迎来到我的Github，如果你也对工业4.0或者IoT感兴趣可以通过以下方式联系我：<br>
Welcome to my Github, if you are interested in Industrial 4.0 and IoT as well, please feel free to contact me: <br>
Location: @Shanghai, China<br>
Email: maydaymiao@126.com<br>
Linkedin: https://www.linkedin.com/profile/in/michael-miao-21939749

# Raspberry-Pi
## **Catalogue**
* [1. Hardware](#1)
* [2. Pre-config](#2)
  * [2.1. Putty and TightVNC Viewer](#2.1)
  * [2.2. Config.txt](#2.2)
* [3. Sensor Project](#3)
  * [3.1. First Project - DS18B20 Temperature Sensor](#3.1)
  * [3.2. I2C - BM180 Environment Sensor](#3.2)
  * [3.3. Character LCD](#3.3)
* [4. Communication Protocol](#4)
  * [4.1. REST](#4.1)
  * [4.2. MQTT](#4.2)


##<h2 id="1">1. Hardware</h2>
Raspberry Pi 3, 32GB MicroSD Card, 5inch-HDMI-LCD, Breadboard, DS18B20, BM180, Mouse and Keyboard

![](https://github.com/maydaymiao/Raspberry_Pi/blob/master/image/hardware.jpg)

##<h2 id="2">2. Pre-config</h2>
###<h3 id="2.1">2.1 Putty and TightVNC Viewer</h3>
As it is quite slow to access to orignal Raspbian source from China, you can switch to China local source, here I use Aliyun.<br>
`sudo nano /etc/apt/sources.list`<br>
Replace the contents with below,<br>
`deb http://mirrors.aliyun.com/raspbian/raspbian/ wheezy main non-free contrib`<br>
`deb-src http://mirrors.aliyun.com/raspbian/raspbian/ wheezy main non-free contrib`<br>
Then run: `sudo apt-get update && apt-get upgrade -y`<br><br>
Download and install Putty.exe from: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html. You can find the IP address of your Raspberry Pi from your router list and connect Putty with your device, the inital username and password for Raspberry Pi is "pi" and "raspberry".<br><br>
In order to has a remote GUI view of your Rapsberry Pi, I use a tool called VNC, you can download from: http://www.tightvnc.com/download.php. <br><br>
Before connecting to VNC, you have to firstly run `sudo apt-get install tightvncserver` in putty, and then run `vncserver -geometry 1024x768`, it will ask you to set a password for remoting at the first time. 


###<h3 id="2.2">2.2 Config.txt</h3>
The default keyboard layout of Raspberry Pi is British keyboard, you can follow below steps to change to US setting.<br>
1. `sudo raspi-config`<br>
2. Select International Options<br>
3. Select Generic 104-key PC<br>
4. Select Other<br>
5. Select English(US)<br>
6. Scroll to the top and select English(US)<br>
7. Select default, no compose key, yes<br>
8. `sudo reboot`<br>

As I have a 5Inch-LCD, but the initial image window does not fit to my screen (only 3/4 size), you can follow the below steps if you meet this issue as well. If you are using other size, please just skip<br>
run `sudo nano /boot/config.txt`<br><br>
`# uncomment if hdmi is not detected and composite is being output`<br>
`hdmi_force_hotplug=1`<br><br>
`# uncomment to force a specific HDMI mode (here we are forcing 800*480)`<br>
`hdmi_group=2`<br>
`hdmi_mode=1`<br>
`hdmi_mode=87`<br>
`hdmi_cvt 800 480 60 6 0 0 0`<br><br>
`start_file=start_x.elf`<br>
`fixup_file=fixup_x.elf`<br>
`#gpu mem=128`<br><br>
run `sudo reboot`<br>

##<h2 id="3">3. Project</h2>
##<h3 id="3.1">3.1. First Project - DS18B20 Temperature Sensor</h3>
####Hardware####
DS18B20 sensor and a 4.7K resistor. You can also use a DS18B20 module which embeded the resistor inside, and that is my choice as well. 

![](https://github.com/maydaymiao/Raspberry_Pi/blob/master/image/DS18B20.jpg)

####Add OneWire support####
1. Run `sudo nano /boot/config.txt`, Scrolling to the bottom and typing `dtoverlay=w1-gpio` there and then run `sudo reboot`.
2. When the device is back up, type the commands below into terminal. After that, you should be able to see YES at the end of the first line and the temperature will be at the end of the second line, in 1/000 degrees C.
```linux
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls
cd 28-xxxx (change this to match what serial number pops up, you can type 28 and click "tab")
cat w1_slave
```

####Python Project####
Please refer to: https://github.com/maydaymiao/Raspberry_Pi/blob/master/DS18B20_Temperature_Sensor.py<br>
You can remove the blank space for the last two statements if you would like to print the real time value on the screen.
```python
while True:        
    print(read_temp())
```
![](https://github.com/maydaymiao/Raspberry_Pi/blob/master/image/temp.png)

##<h3 id="3.2">3.2. I2C - BM180 Environment Sensor</h3>

![](https://github.com/maydaymiao/Raspberry_Pi/blob/master/image/BMP180_Wiring.jpg)
I2C is a very commonly used standard designed to allow one chip to talk to another. If this is your first time to connect I2C to the Pi, please follow below steps.<br>
```linux
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
sudo raspi-config
Advanced Options - I2C - Enable
sudu reboot
```
####Testing I2C
`sudo i2cdetect -y 1`<br>
If you can see the number in the address (show up at 0x77), which means you have already connected the I2C. One tip is that if it is not showing after go through my steps, try to press tight the sensor into your breadboard.<br>
![](https://github.com/maydaymiao/Raspberry_Pi/blob/master/image/I2C.png)

####Using the Adafruit BMP Python Library
```linux
sudo apt-get update
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python setup.py install
cd examples
sudo python simpletest.py
```
![](https://github.com/maydaymiao/Raspberry_Pi/blob/master/image/BM180_Sample.png)

##<h3 id="3.3">3.3. Character LCD</h3>
From this tutorial, you will learn how to send message to a character LCD and display the temperature and pressure data from above BM180 project to LCD
####Hardware
16*2 LCD, breadboard, connecting pins and potentiometer (in Chinese, it is called as "电位器")<br>
####Wiring

![](https://github.com/maydaymiao/Raspberry_Pi/blob/master/image/LCD_Wiring.png)

* Connect Pi 5V power to the power rail of the breadboard. From the power rail connect one outer lead of the potentiometer, LCD pin 2 (VDD), and LCD pin 15 (LED+).
* Connect Pi ground to the ground rail of the breadboard. From the ground rail connect the other outer lead of the potentiometer, LCD pin 1 (VSS), LCD pin 5 (R/W) and LCD pin 16.
* Connect the middle lead of the potentiometer to LCD pin 3 (V0/contrast) and left right to ground and 5V power.
* Connect Pi pin 27 to LCD pin 4 (RS).
* Connect Pi pin 22 to LCD pin 6 (E/clock enable).
* Connect Pi pin 25 to LCD pin 11 (DB4).
* Connect Pi pin 24 to LCD pin 12 (DB5).
* Connect Pi pin 23 to LCD pin 13 (DB6).
* Connect Pi pin 18 to LCD pin 14 (DB7).

####Dependencies
```linux
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip git       #You can ignore any warnings about dependencies already being installed.
sudo pip install RPi.GPIO
```
####Installation
Once the dependencies above have been installed you can install the character LCD module by executing the following commands on the device:
```linux
cd ~
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
cd Adafruit_Python_CharLCD
sudo python setup.py install
```
####Usage
Once the library is installed you can find a few examples of its usage in the examples subdirectory. If you're using a monochrome backlight LCD (i.e. single color, like a white on blue LCD) the char_lcd.py script will demonstrate the basic usage, and you can ignore the backlight pin definition in the script as monochrome LCD does not have that.<br>
To run the example execute:<br>
```linux
cd examples
python char_lcd.py
```
You should see the LCD backlight turn on and messages printed to the display.

####Showing current time, temperature and pressure data in the LCD


##<h2 id="4">4. Communication Protocol</h2>
###<h3 id="4.1">4.1. REST</h3>
###<h3 id="4.2">4.2. MQTT</h3>
####Mosquitto
Here is a very good introduction for MQTT: https://www.baldengineer.com/mqtt-introduction.html<br>
Eclipse Mosquitto™ is an open source (EPL/EDL licensed) message broker that implements the MQTT protocol versions 3.1 and 3.1.1. MQTT provides a lightweight method of carrying out messaging using a publish/subscribe model. This makes it suitable for "Internet of Things" messaging such as with low power sensors or mobile devices such as phones, embedded computers or microcontrollers like the Arduino.
```linux
wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
sudo apt-key add mosquitto-repo.gpg.key
cd /etc/apt/sources.list.d/
sudo wget http://repo.mosquitto.org/debian/mosquitto-jessie.list
sudu apt-get update
sudo apt-get install mosquitto
```
You may get an error message when go through the last step above: "Depends: libwebsockets3 (>= 1.2) but it is not installable". To solve this error, please follow below steps.<br>
```linux
wget http://ftp.cn.debian.org/debian/pool/main/libw/libwebsockets/libwebsockets3_1.2.2-1_armhf.deb
sudo dpkg -i libwebsockets3_1.2.2-1_armhf.deb
sudo apt-get install mosquitto
```
You can run `netstat -tln | grep 1883` to verify the installation, if you can see the same as below which means you have successfully installed Mosquitto broker.
![](https://github.com/maydaymiao/Raspberry_Pi/blob/master/image/mqtt_broker.png)

####Paho Client
The Eclipse Paho project provides open-source client implementations of MQTT and MQTT-SN messaging protocols aimed at new, existing, and emerging applications for the Internet of Things (IoT). Follow below steps to install Paho on your Pi.<br>
```linux
pip install paho-mqtt
git clone https://github.com/eclipse/paho.mqtt.python.git
cd /home/pi/paho.mqtt.python/
sudo python setup.py install
```
To verify the installation of Paho, you can do this:<br>
`git clone https://github.com/maydaymiao/Raspberry_Pi.git`<br>
You can either run in the terminal, or go to the MQTT folder, firstly run the Publisher.py, then run the Subscriber.py. Please do remember fill your Pi's IP address into "MQTT BROKER". You shoud able to see the same as below.<br>
![](https://github.com/maydaymiao/Raspberry_Pi/blob/master/image/Paho.png)

