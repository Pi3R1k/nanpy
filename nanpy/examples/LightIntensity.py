#!/usr/bin/env python2

from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager

from nanpy.bh1750fvi import Bh1750Fvi
from time import sleep

connection = SerialManager(device='/dev/rfcomm0')

## Devices Address
#Device address when address pin LOW : 0x23 
#Device address when address pin HIGH : 0x5C

aTree = ArduinoTree(connection=connection)
aApi = ArduinoApi(connection=connection)

bh = Bh1750Fvi(aTree.wire)
aApi.pinMode(13, aApi.OUTPUT)

# Device 1 
#aApi.digitalWrite(9, HIGH) 
#bh.SetAddress(0x5C)

# Device 2
aApi.digitalWrite(9, LOW) 
bh.SetAddress(0x23)

## Light intensity modes 
#Continuous_H_resolution_Mode : 0x10
#Continuous_H_resolution_Mode2 : 0x11
#Continuous_L_resolution_Mode : 0x13
#OneTime_H_resolution_Mode : 0x20
#OneTime_H_resolution_Mode2 : 0x21
#OneTime_L_resolution_Mode : 0x23

# Continuous
bh.SetMode(0x10)
sleep(0.05)
print("Continuous_H_resolution_Mode %s lux" % bh.GetLightIntensity())

bh.SetMode(0x11)
sleep(0.05)
print("Continuous_H_resolution_Mode2 %s lux" % bh.GetLightIntensity())

bh.SetMode(0x13)
sleep(0.05)
print("Continuous_L_resolution_Mode %s lux" % bh.GetLightIntensity())

# OneTime
bh.SetMode(0x20)
sleep(0.05)
print("OneTime_H_resolution_Mode %s lux" % bh.GetLightIntensity())

bh.SetMode(0x21)
sleep(0.05)
print("OneTime_H_resolution_Mode2 %s lux" % bh.GetLightIntensity())

bh.SetMode(0x23)
sleep(0.05)
print("OneTime_L_resolution_Mode %s lux" % bh.GetLightIntensity())

