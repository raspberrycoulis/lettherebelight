#!/usr/bin/env python

# Import the necessary modules, including the Enviro pHAT module
import os
import time
from envirophat import light

# Variables used defined below
lux = 250        # Light level to trigger action
state = 0        # Logic to tell whether the light is on or off
period = 0.10    # Time (in seconds) between checks. Default is 0.10.

def lights_on():
  os.system('curl -s "http://username:password@PI-IP-ADD-RESS/api-all-on/" > /dev/null')
  print('Lights on!')
  
def lights_off():
  os.system('curl -s "http://username:password@PI-IP-ADD-RESS/api-all-off/" > /dev/null')
  print('Lights off!')

while True:
  if light.light() < lux and state != 1:
      lights_on
      state = 1
  elif light.light() >= lux and state == 1:
      lights_off
      state = 0
  time.sleep(period)
