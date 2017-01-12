# vim: sw=4 ts=4 ft=python et
import iot_carbon_client

PIN = 4

def client(server = "8.8.8.8", port = 2003, deepsleep = False, interval = 60):
    iot_carbon_client.carbon_client(server, port, deepsleep, measure_n_send, interval)

def dew_point(celsius, humidity):
    # reference: http://en.wikipedia.org/wiki/Dew_point
    # delta max = 0.6544 wrt dewPoint()
    from math import log

    a = 17.271
    b = 237.7
    temp = (a * celsius) / (b + celsius) + log(humidity*0.01)
    return (b * temp) / (a - temp);

def measure_n_send(sock, send_cb):
    import dht
    import gc
    import machine

    sensor = dht.DHT22(machine.Pin(PIN))
    sensor.measure()
    
    t = round(sensor.temperature(), 1)
    send_cb(sock, 'temperature', t)

    h = round(sensor.humidity(), 1)
    send_cb(sock, 'humidity', h)

    d = round(dew_point(t, h), 1)
    send_cb(sock, 'dew_point', d)

    v = round(machine.ADC(1).read()/1000, 3)
    send_cb(sock, 'Vcc', v)

