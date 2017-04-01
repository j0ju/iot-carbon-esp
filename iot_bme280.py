# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

import machine
import carbon
import iot
import bme280

# reference: http://en.wikipedia.org/wiki/Dew_point
# delta max = 0.6544 wrt dewPoint()
def dew_point(celsius, humidity):
    from math import log

    a = 17.271
    b = 237.7
    temp = (a * celsius) / (b + celsius) + log(humidity*0.01)
    return (b * temp) / (a - temp);

def main( INTERVAL = 7,
          DEEPSLEEP = False,
          I2C_SDA_PIN = 4,
          I2C_SCL_PIN = 5):
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        print(b'sleep: awoke from DEEP SLEEP')

    c = carbon.client()
    i = machine.I2C(scl=machine.Pin(I2C_SCL_PIN), sda=machine.Pin(I2C_SDA_PIN))
    s = bme280.BME280(i2c=i)

    while True:
        (t, p, h) = s.read_compensated_data()

        t = t/100                      # C
        p = p/25600                    # hPa
        h = h/1024                     # rel%
        d = dew_point(t, h)            # C
        v = machine.ADC(1).read()/1000 # V

        carbon.send(c, b'Vcc', v)
        carbon.send(c, b'temperature', t)
        carbon.send(c, b'pressure', p)
        carbon.send(c, b'humidity', h)
        carbon.send(c, b'dew_point', d)

        if DEEPSLEEP:
            c.close()

        #import gc
        #import micropython
        #gc.collect()
        #micropython.mem_info()

        iot.sleep(INTERVAL, DEEPSLEEP)

# vim: sw=4 ts=4 ft=python et foldmethod=indent
