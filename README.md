# ESP32-433Mhz-Transmitter

A pure microPython RF Transmitter.

This transmit tool based on a config file where you combine user friendly name and used protokols.  
Copy both files and the encoder directory to your ESP32  
In your application import the module:   
from tx433_esp.py import *  

Call it with ESPtx(name) name is the user friendly name out of the tx433_config.py  
eg. ESPtx(Switch_on)

Futher as an expert you can create and add your own encoder files in the directory tx433_encoder
I have implemented a power socket Quigg7000, the ev1527 protokoll and a spezial encoder for a remote bell.
Feel free to implement your own.

