# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

import machine
import temp_helper
import dht

class Dht22Sensor():
    def __init__(self, pin = 4):
        self.dht = dht.DHT22(machine.Pin(pin))

    def keys(self):
        measured = False
        # sometimes the sensor needs some time to start and does not react on the first
        # .measure call
        try:
            self.dht.measure()
        except Exception as e:
            self.dht.measure()

        return [ 'temperature', 'humidity', 'dew_point' ]

    def value(self, key):
        if key == 'temperature':
            return self.dht.temperature()
        elif key == 'humidity':
            return self.dht.humidity()
        elif key == 'dew_point':
            t = self.dht.temperature()
            h = self.dht.humidity()
            return temp_helper.dew_point(t, h)

# vim: sw=4 ts=4 ft=python et foldmethod=indent
