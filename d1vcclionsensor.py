# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

import machine

class D1VccLiOnSensor():

    # scale: is factor to correct the measured Vcc
    #  default is 1.0718 for Wemos D1 battery shield v1.1.0
    #  those have a 100+220+130 Ohm voltage devider

    def __init__(self, scale = 1.0718):
        self.scale = scale

    def keys(self):
        return [ 'Vcc' ]

    def value(self, key):
        if key == 'Vcc':
            return machine.ADC(0).read()*4.2/1024*self.scale

# vim: sw=4 ts=4 ft=python et foldmethod=indent
