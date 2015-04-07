from __future__ import division

import logging
from nanpy.i2c import I2C_Master

log = logging.getLogger(__name__)

class Bh1750Fvi(object):

    def __init__(self, wire):
        self.i2c = I2C_Master(wire)

    def read_bytes(self, count):
        x = self.i2c.request(self.address, count)
        return x

    def write_byte(self, data):
        self.i2c.send(self.address, [data])
    
    def SetAddress(self, address):
        self.address = address

    def SetMode(self, mode):
	self.write_byte(mode)

    def GetLightIntensity(self):
	data = self.read_bytes(0x11)
    	lux = round((data[1] + (256 * data[0])) / 1.2)
  	return lux;

