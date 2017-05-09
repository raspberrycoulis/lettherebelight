#!/usr/bin/env python

# To Do: Define the lux level for the lights to turn on and off.

# Import the necessary modules, including the Enviro pHAT module
import os
import time
from envirophat import light

period = 900    # Time (in seconds) between checks. Default is 15 minutes.

def lights():
  while True:
    lux = light.light()
    if lux <= 7:  # Set the light level to check for - if the level falls below this, it will activate the lights
        print ("Let there be light!")
        #print ("Light={0:.0f} lux".format(lux)) # Keeping here to remind me for the time being
        try:
          os.system('curl -s "http://username:password@PI-IP-ADD-RESS/api-all-on/" > /dev/null')
        except Exception:
          ## Process exception here
          print ("Error getting light level!")
    
    elif lux >= 50:
        print ("We don't need the lights on any more!")
        try:
          os.system('curl -s "http://username:password@PI-IP-ADD-RESS/api-all-off/" > /dev/null')
        except Exception:
          print ("Error getting light level!")
    
    else:
        print ("Hmm, I'm not sure!")
        #print ("Light={0:.0f} lux".format(lux)) # Keeping here to remind me for the time being

    #Sleep some time
    time.sleep( period )

lights()
