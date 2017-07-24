import iotcollector
c = iotcollector.IoTCollector()
c.interval = 7

import ttydelivery
d = ttydelivery.TtyDelivery()
#d.deliverNonNumericValues = False
c.addDelivery(d)

import vccsensor
s = vccsensor.VccSensor()
c.addSensor(s)

import bme280sensor
s = bme280sensor.Bme280Sensor(sda = 4, scl = 5)
c.addSensor(s)

c.run()
