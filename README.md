欢迎来到我的Github，如果你也对工业4.0或者IoT感兴趣可以通过以下方式联系我：<br>
Welcome to my Github, if you are interested in Industrial 4.0 and IoT as well, please feel free to contact me: <br>
Location: @Shanghai, China<br>
Email: maydaymiao@126.com<br>
Linkedin: https://www.linkedin.com/profile/in/michael-miao-21939749

# Raspberry-Pi
## catalogue
* [1. Hardware](#1)
* [2. Pre-config](#2)
  * [2.1. Putty and TightVNC Viewer](#2.1)
  * [2.2. Config.txt](#2.2)


##<h1 id="1">1. Hardware</h1>
Raspberry Pi 3, 32GB MicroSD Card, 5inch-HDMI-LCD, Breadboard, DS18B20, BM180, Mouse and Keyboard

![](https://github.com/maydaymiao/Raspberry_Pi/blob/master/image/hardware.jpg)

##<h2 id="2">2. Pre-config</h2>
###<h3 id="2.1">2.1 Putty and TightVNC Viewer</h3>
Download and install Putty.exe from: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html. You can find the IP address of your Raspberry Pi from your router list and connect Putty with your device, the inital username and password for Raspberry Pi is "pi" and "raspberry".<br><br>
In order to has a remote GUI view of your Rapsberry Pi, I use a tool called VNC, you can download from: http://www.tightvnc.com/download.php. <br><br>
Before connecting to VNC, you have to firstly run `sudo apt-get install tightvncserver` in putty, and then run `vncserver -geometry 1024x768`, it will ask you to set a password for remoting at the first time. 


###<h4 id="2.2">2.2 Config.txt</h4>
The default keyboard layout of Raspberry Pi is British keyboard, I change to US setting as I am more used to that.<br>
1. `sudo raspi-config`<br>
2. Select International Options<br>
3. Select Generic 104-key PC<br>
4. Select Other<br>
5. Select English(US)<br>
6. Scroll to the top and select English(US)<br>
7. Select default, no compose key, yes<br>
8. `sudo reboot`<br>
