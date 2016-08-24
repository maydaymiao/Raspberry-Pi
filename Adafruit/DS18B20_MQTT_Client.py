# Import standard python modules.
import random
import sys
import time

# Import Adafruit IO MQTT Client.
from Adafruit_IO import MQTTClient

# Import function from DS18B20_Temperature_Sensor.py
from DS18B20_Temperature_Sensor import read_temp

# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY = 'your ADAFRUIT_IO_KEY'
ADAFRUIT_IO_USERNAME = 'your ADAFRUIT_IO_USERNAME'

# Define callback functions which will be called when certain events happen.
def connected(client):
    print 'Connected to Adafruit IO! Listening for Raspberry_Pi_MQTT changess...'
    # Subscribe to changes on a feed named MQTT_Feed
    client.subscribe('Raspberry_Pi_MQTT')

def disconnected(client):
    print 'Disconnected from Adafruit IO!'
    sys.exit(1)

def message(client,feed_id,payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has the new value.
    print 'Feed {0} received new value: {1}'.format(feed_id,payload)

# Create an MQTT client instance.
client = MQTTClient('your ADAFRUIT_IO_KEY','ADAFRUIT_IO_USERNAME')

# Setup the callback functions defined above,
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

# Connect to the Adafruit IO server.
client.connect()

# Now the program needs to use a client loop function to ensure messages are sent and received.
client.loop_background()
# Now send new values every 10 seconds.
print 'Publishing a new message every 5 seconds (press Ctrl-C to quit)...'
var=1
while var==1:       
    client.publish('Raspberry_Pi_MQTT',read_temp())
    time.sleep(5)
