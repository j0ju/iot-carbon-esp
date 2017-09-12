# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

import machine

class D1VccLiOnSensor():
    def keys(self):
        return [ 'Vcc' ]

    def value(self, key):
        if key == 'Vcc':
            return machine.ADC(0).read()*4.2/1024

# vim: sw=4 ts=4 ft=python et foldmethod=indent
