


from TX_config import *

def connect(ssid,password):
    import network
    import time
    import machine

    
    station = network.WLAN(network.STA_IF)  # Now the File exist so make Connection 

    if station.isconnected() == True:
      print("Schon verbunden")
      return

    station.active(True)

    if len(ip) > 7:      # mit fester IP
       station.ifconfig((ip,subnet,gateway,dns))
    station.connect(ssid,password)
    station.isconnected()
    count=0
    while not station.isconnected():
      time.sleep(0.5)
      #print("*",end="")
      count+=1
      if count> 10: # Error open connection from File
        break 
    print(station.ifconfig()) 
    return (station.isconnected())

def disconnect():
    import network
    station = network.WLAN(network.STA_IF)
    station.disconnect()
    station.active(False)
    #print("WiFi off!")



























