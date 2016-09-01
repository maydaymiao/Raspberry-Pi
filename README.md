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
`deb-src http://mirrors.aliyun.com/raspbian/raspbian/ wheezy main non-free contrib`<br><br>
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


