#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time
import Adafruit_CharLCD as LCD
from datetime import datetime
from subprocess import *
import Adafruit_BMP.BMP085 as BMP085

# Raspberry Pi pin configuration:
lcd_rs        = 27  
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)


# Showing welcome message
lcd.message('Welcome to \nMichael\'s home')
time.sleep(1.5)

# Showing time
lcd.clear()
lcd.message(datetime.now().strftime('%b %d  %H:%M:%S'))
time.sleep(1.5)


# Showing temperature & Pressure
lcd.clear()
sensor = BMP085.BMP085()
lcd.message('Temp: %s C\n' % sensor.read_temperature())
lcd.message('Pressure: %s' % sensor.read_pressure())
time.sleep(2)

# Scrolling message
lcd.clear()
message = 'Goodbye'
lcd.message(message)
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_right()
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_left()

