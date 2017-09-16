import iotcollector
c = iotcollector.IoTCollector(deepsleep = True)
#c.debug = True
c.interval = 57

import carbondelivery
d = carbondelivery.CarbonDelivery(server = '10.23.43.5')
d.debug = True
c.addDelivery(d)

import D1VccLiOnSensor
s = D1VccLiOnSensor.D1VccLiOnSensor()
c.addSensor(s)

import bme280sensor
s = bme280sensor.Bme280Sensor(sda = 4, scl = 5)
c.addSensor(s)

c.run()

