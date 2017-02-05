# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

# global config
import CONFIG

# DHT config
PIN        = 2
POWER_PIN  = 0

import machine
import iot_carbon as carbon
import dht
import iot

# reference: http://en.wikipedia.org/wiki/Dew_point
# delta max = 0.6544 wrt dewPoint()
def dew_point(celsius, humidity):
    from math import log

    a = 17.271
    b = 237.7
    temp = (a * celsius) / (b + celsius) + log(humidity*0.01)
    return (b * temp) / (a - temp);

def dht11_powerup(pin):
    p = machine.Pin(pin, machine.Pin.OUT)
    p.value(1)
def dht11_powerdown(pin):
    p = machine.Pin(pin, machine.Pin.OUT)
    p.value(0)

def dht11_get(pin, retries = CONFIG.RETRIES):
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

c = carbon.client()
dht11_powerup(POWER_PIN)
while True:
    s = dht11_get(PIN, CONFIG.RETRIES)

    t = s.temperature()
    h = s.humidity()
    d = dew_point(t, h)
    # this needs executed once
    #   import adc_mode
    #   adc_mode.set(adc_mode.ADC_MODE_VCC)
    v = machine.ADC(1).read()/1000

    carbon.send(c, 'Vcc', v)
    carbon.send(c, 'temperature', t)
    carbon.send(c, 'humidity', h)
    carbon.send(c, 'dew_point', d)

    c.close()

    import gc
    gc.collect()

    iot.sleep(CONFIG.INTERVAL, CONFIG.DEEPSLEEP)

# vim: sw=4 ts=4 ft=python et foldmethod=indent
