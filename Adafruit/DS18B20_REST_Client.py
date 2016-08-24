import time

# Import Adafruit IO REST Client
from Adafruit_IO import Client

# Import function from DS18B20_Temperature_Sensor.py
from DS18B20_Temperature_Sensor import read_temp

# Set to your Adafruit IO Key
Adafruit_IO_Key = 'your Adafruit_IO_Key'

# Create an instance of the REST client.
aio=Client('your Adafruit_IO_Key')

# Send a value to the feed 'Raspberry_Pi'. This will create the feed if it doesn't exist already
var=1
while var==1:
  aio.send('Raspberry_Pi',read_temp())
  time.sleep(5)
