import os
import glob
import time
import subprocess

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Create a file to store the temperature data
base_dir='/sys/bus/w1/devices/'
device_folder=glob.glob(base_dir+'28*')[0]
device_file=device_folder+'/w1_slave'

# Read the data from that file
def read_temp_raw():
    f=open(device_file,'r')
    lines=f.readlines()
    f.close()
    return lines

# There will be two lines for each packet, at the end of the first line which is lines[0] includes YES or NO indicates the response quality,
# If it is yes, then the temperature will be at the end of the second line, in 1/000 degrees C.
def read_temp():
    lines=read_temp_raw()
    while lines[0].strip()[-3:]!='YES':
        time.sleep(0.2)
        lines=read_temp_raw()
    equals_pos=lines[1].find('t=')
    if equals_pos!=-1:
        temp_string=lines[1][equals_pos+2:]
        temp=float(temp_string)/1000.0
        return temp    
    while True:        
        print(read_temp())
