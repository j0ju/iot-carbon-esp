# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

# global config
import CONFIG

# config
DHT_PIN     = 0
I2C_SCL_PIN = 5
I2C_SDA_PIN = 4
POWER_PIN   = 2

import machine
import iot_carbon as carbon
import dht
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

def powerup(pin):
    p = machine.Pin(pin, machine.Pin.OUT)
    p.value(1)

def dht_get(pin, retries = CONFIG.RETRIES):
    import machine
    for i in range(1, retries):
        try:
            s = dht.DHT11(machine.Pin(pin))
            s.measure()
            break
        except Exception as e:
            import time
            s = None
            time.sleep(CONFIG.ERROR_WAIT)
    return s

if CONFIG.DEBUG:
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        print('sleep: awoke from DEEP SLEEP')

powerup(POWER_PIN)

c = carbon.client()
dht = dht_get(DHT_PIN, CONFIG.RETRIES)
i2c = machine.I2C(scl=machine.Pin(I2C_SCL_PIN), sda=machine.Pin(I2C_SDA_PIN))

while True:
    bme = bme280.BME280(i2c=i2c)

    (t, p, h) = bme.read_compensated_data()

    t = t/100    # C
    p = p/25600 # hPa

    h = dht.humidity() # rel%

    d = dew_point(t, h)

    # this needs executed once
    #   import adc_mode
    #   adc_mode.set(adc_mode.ADC_MODE_VCC)
    v = machine.ADC(1).read()/1000

    carbon.send(c, 'Vcc', v)
    carbon.send(c, 'temperature', t)
    carbon.send(c, 'pressure', p)
    carbon.send(c, 'humidity', h)
    carbon.send(c, 'dew_point', d)

    c.close()

    if CONFIG.DEBUG:
        bme = None
        import gc
        gc.collect()
        import micropython
        micropython.mem_info()

    iot.sleep(CONFIG.INTERVAL, CONFIG.DEEPSLEEP)

# vim: sw=4 ts=4 ft=python et foldmethod=indent
