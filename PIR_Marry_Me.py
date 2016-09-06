import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

GPIO.setmode(GPIO.BCM)
PIR_PIN=26
LED_PIN=5
GPIO.setwarnings(False)
GPIO.setup(PIR_PIN,GPIO.IN)
GPIO.setup(LED_PIN,GPIO.OUT)

# Raspberry Pi pin configuration:
lcd_rs        = 27  # Note this might need to be changed to 21 for older revision Pi's.
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

def send_message(message):
    lcd.message(message)
    time.sleep(1)

while True:
    if GPIO.input(PIR_PIN):
        lcd.clear()
        GPIO.output(LED_PIN,1)
        print "Motion Detected!"
        message='Yes, I do'
        send_message(message)
        time.sleep(1)
    else:
        lcd.clear()
        GPIO.output(LED_PIN,0)
        message='Will you\n Marray me?'
        send_message(message)
        time.sleep(1)
