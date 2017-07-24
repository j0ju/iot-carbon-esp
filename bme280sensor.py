# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

import machine
import temp_helper
import bme280

class Bme280Sensor():
    def __init__(self, sda = 4, scl = 5):

        i2c = machine.I2C(scl=machine.Pin(scl), sda=machine.Pin(sda))
        self.bme = bme280.BME280(i2c=i2c)

    def keys(self):
        return [ 'temperature', 'humidity', 'pressure', 'dew_point' ]

    def value(self, key):
        (t, p, h) = self.bme.read_compensated_data()
        t = t/100                      # C
        p = p/25600                    # hPa
        h = h/1024                     # rel%

        if key == 'temperature':
            return t
        elif key == 'humidity':
            if h == 0:
                h = float('nan')
            return h
        elif key == 'pressure':
            return p
        elif key == 'dew_point':
            # broken humidity sensor
            if h == 0:
                return float('nan')
            else:
                return temp_helper.dew_point(t, h)

# vim: sw=4 ts=4 ft=python et foldmethod=indent
