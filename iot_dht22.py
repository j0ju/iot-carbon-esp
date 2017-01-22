# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

PIN = 4
INTERVAL = 47
DEEPSLEEP = True
RETRIES = 3
ERROR_WAIT = 1

# reference: http://en.wikipedia.org/wiki/Dew_point
# delta max = 0.6544 wrt dewPoint()
def dew_point(celsius, humidity):
    from math import log

    a = 17.271
    b = 237.7
    temp = (a * celsius) / (b + celsius) + log(humidity*0.01)
    return (b * temp) / (a - temp);

def get_dht22(pin, retries = RETRIES):
    import machine
    for i in range(1, retries):
        try:
            s = dht.DHT22(machine.Pin(pin))
            s.measure()
            break
        except Exception as e:
            import time
            s = None
            time.sleep(ERROR_WAIT)
    return s

while True:
    import carbon
    import dht
    import machine
    import iot

    c = carbon.client()
    s = get_dht22(PIN, RETRIES)
         
    t = s.temperature()
    h = s.humidity()
    d = dew_point(t, h)
    # this needs executed once
    #   import adc_mode
    #   adc_mode.set(adc_mode.ADC_MODE_VCC)
    v = machine.ADC(1).read()/1000
    
    t = "%.1f" % ( t )
    h = "%.1f" % ( h )
    d = "%.1f" % ( d )
    v = "%.3f" % ( v )

    carbon.send(c, 'Vcc', v)
    carbon.send(c, 'temperature', t)
    carbon.send(c, 'humidity', h)
    carbon.send(c, 'dew_point', d)

    c.close()

    iot.sleep(INTERVAL, DEEPSLEEP)

    import gc
    gc.collect()

# vim: sw=4 ts=4 ft=python et foldmethod=indent
