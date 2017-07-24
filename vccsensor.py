# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

import machine

class VccSensor():
    def keys(self):
        return [ 'Vcc' ]

    def value(self, key):
        if key == 'Vcc':
            return machine.ADC(1).read()/1000

# vim: sw=4 ts=4 ft=python et foldmethod=indent
