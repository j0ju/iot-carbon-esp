import iotcollector
c = iotcollector.IoTCollector()
c.interval = 10

import ttydelivery
d = ttydelivery.TtyDelivery()
c.addDelivery(d)

import vccsensor
s = vccsensor.VccSensor()
c.addSensor(s)

import dht22sensor
s = dht22sensor.Dht22Sensor()
c.addSensor(s)

c.run()
