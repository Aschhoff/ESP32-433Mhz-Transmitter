



import esp
#esp.osdebug(None)
#from neo import *

import time
from machine import Pin
led = Pin(2, Pin.OUT)
#neo("gelb")
led.on()
time.sleep(1)


err_conf=0
err_wifi=0
result=""


try:
    from TX_config import *
    print(ssid) # loest Fehler aus!
except:
    err_conf=1
    #neo("rot")
    for n in range(5):
      led.off()
      time.sleep(0.5)
      led.on()
      time.sleep(0.5)
      
    print("TX_config?")

if err_conf==0: 
  import wifi
  try:
      result=wifi.connect(ssid,password)
      time.sleep(1) 
      wifi.disconnect()
      time.sleep(1)
  except:
      #neo("blau") 
      for n in range(10):
       led.off()
       time.sleep(0.2)
       led.on()
       time.sleep(0.2)
      err_wifi=1
      print("WiFi?")

if err_wifi==0 and result:
    #neo("gruen")
    led.off()
    import IR_TX433_ESP























