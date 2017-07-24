# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

class IoTCollector():
    def __init__(self, interval = 60, deepsleep = False):
        self.interval = interval
        self.deepsleep = deepsleep
        self.delivery = []
        self.sensors = []

    def run(self):
        import iotesp
        while True:
            for sensor in self.sensors:
                for key in sensor.keys():
                    for delivery in self.delivery:
                        delivery.send(key, sensor.value(key))

            if self.deepsleep:
                for delivery in self.delivery:
                    delivery.close()
            iotesp.sleep(self.interval, self.deepsleep)

    def addDelivery(self, delivery):
        self.delivery.append(delivery)

    def addSensor(self, sensor):
        self.sensors.append(sensor)

# vim: sw=4 ts=4 ft=python et foldmethod=indent
