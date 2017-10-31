#!/usr/bin/env python

# Import the necessary modules, including the Enviro pHAT module
import os
import time
from envirophat import light

# Variables used defined below

state = 0       # Logic to tell whether the light is on or off.
period = 15     # Time (in seconds) between checks. Default is 15 seconds.

def lights_on():
  os.system('curl -s "http://username:password@PI-IP-ADD-RESS/api-all-on/" > /dev/null')
  print('Lights on! Room luminence is {0:.0f} lux.'.format(light.light()))

def lights_off():
  os.system('curl -s "http://username:password@PI-IP-ADD-RESS/api-all-off/" > /dev/null')
  print('Lights off! Room luminence is {0:.0f} lux.'.format(light.light()))

lux = 250       # Defines when the lights will come on or off.

while True:
  if light.light() < lux and state != 1:
      lights_on()
      state = 1
  elif light.light() >= lux and state == 1:
      lights_off()
      state = 0
  time.sleep(period)
