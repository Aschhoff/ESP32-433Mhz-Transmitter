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
    
#---------------------------- Main -----------------------------------
def ESPtx(uname):
    dev=""
    if uname!="rawdata":
      dev=devices[uname]
      if dev!="":
        devdata=json.dumps(dev)
        bef=dev["prot"]+".code("+devdata+")" # erkanntes Protokoll in bef
        data=eval(bef)   # eval => ausfueren von String bef als Befehl

    else:
      dataraw=devices[uname] 
      data=dataraw["sync"],dataraw["short"],dataraw["long"],dataraw["code"]
    print(data)
    tx433(data,tx)

#---------------------------- init -----------------------------------

from machine import Pin,time_pulse_us
import time
import json
import os
import sys

# lade config.py mit Protokoll und Pattern
# aus config importiere die Dekoder Module
from tx433_config import * # importiere config mit var Namen

tx = Pin(tx_pin,Pin.OUT)

# aus Path rx433_encoder Encoder Module

protokolle={}

sys.path.append("./tx433_encoder")
dirs = os.listdir( "./tx433_encoder")
for prot in dirs:
  if prot[-3:]==".py":
    a=prot[:-3]   # Name des Dekodiermoduls aus Dir tx433_encoder
    locals()[a]=__import__(a)
    # erzeuge locale Variable aus String a => 
    # import modul mit Name aus Variable a

#---------------------------------------------------------------------

if __name__== "__main__":

    uname="Bell"
    ESPtx(uname)














