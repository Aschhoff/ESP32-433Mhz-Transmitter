


# Detlev Aschhoff info@vmais.de
# The MIT License (MIT)
#
# Copyright (c) 2020
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


#----------------------------- Puls Detection ---------------------------
def irBin(rx):
  puls=0
  data_raw=[]
  print("Receive......")
  while puls<4400 or puls > 4600:
    puls=time_pulse_us(rx,1) 
  while puls<30000:
    puls=time_pulse_us(rx,1)
    data_raw.append(puls)
  return data_raw
# Output: Liste der Impulslaengen   


def analyse(rx):
  while -1:
    data_raw=irBin(rx)
    list_binary=[]
    list_str=""
    #print(data_raw)
    if len(data_raw)==33:
      for n in range(len(data_raw)-1):
        if data_raw[n]<800:
          list_binary.append("0")      # Null in Liste 
        if data_raw[n]>1200:
          list_binary.append("1")      # Eins in Liste
      list_str="".join(list_binary)    # String aus Liste          
      return list_str
  return "error"


def tx433(data,tx):
    sync=int(data[0])
    short=int(data[1])
    long=int(data[2])
    code=data[3]

    tx.value(0)
    for t in range(5):
        tx.value(1)                 #header
        time.sleep_us(short)

        for i in code:
          if i == '0':
            tx.value(0)
            time.sleep_us(short)
            tx.value(1)
            time.sleep_us(long)
          elif i == '1':
            tx.value(0)
            time.sleep_us(long)
            tx.value(1)
            time.sleep_us(short)
          else:
            continue
        tx.value(0)     #Footer
        time.sleep_us(sync)
        tx.value(1)
    tx.value(0)

  
def ESPtx(uname):
    dev=""
    if uname!="rawdata":
      dev=devices[uname]
      if dev!="":
        devdata=json.dumps(dev)
        bef=dev["prot"]+".code("+devdata+")" # Aufruf Encoder xxx.code(Daten)
        data=eval(bef)   # eval => ausfueren von String bef als Befehl

    else:
      dataraw=devices[uname] 
      data=dataraw["sync"],dataraw["short"],dataraw["long"],dataraw["code"]

    tx433(data,txRF)
    
    return "_OK_"
#-------------------------------------------------------------------


import time
import json
import wifi
import socket
import os
import sys
import gc
from machine import Pin,time_pulse_us
from TX_config import * # importiere config mit var Namen
txRF = Pin(TX433,Pin.OUT)
rxIR = Pin(IRrx,Pin.IN,Pin.PULL_UP)    # Input Pin


protokolle={}

sys.path.append("./TX_encoder")
dirs = os.listdir( "./TX_encoder")
for prot in dirs:
  if prot[-3:]==".py":
    a=prot[:-3]   # Name des Encodermoduls aus Dir x_encoder
    locals()[a]=__import__(a)
    # erzeuge locale Variable aus String a => 
    # import modul mit Name aus Variable a
    
    
print("------------------ TX ---------------------")

wifi.connect(ssid,password)
time.sleep(1)

#sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
#sock.bind(("",8888))
#sock.listen(1)
#sock.setblocking(0)

try:  
  while True: 
    data=""

    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
    sock.bind(("",8888))
    sock.listen(1)
    print("waiting ...")
    conn, addr = sock.accept() 
    data=conn.recv(128)
    print(data)
    data=data.decode()    # Format {'cmd':'kommando'}
    if data !="":
      datadict=eval(data)
      bef=datadict["cmd"]
      
      if bef=="irx":
        binString = analyse(rxIR)
        print(binString)
        conn.send("==> "+binString+chr(10))
      else:
        print(addr[0],"--> ",bef)
        dummy=ESPtx(bef)
        print(dummy)
        conn.send("==> "+bef+" OK"+chr(10))
    sock.close()
    gc.collect()
    
except KeyboardInterrupt:
    sock.close()
    pass  
finally:
    sock.close()
    print('Close socket')















