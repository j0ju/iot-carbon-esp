# vim: sw=4 ts=4 ft=python et

INTERVAL = 60
ERROR_WAIT = 5
METRIC_FMT = "iot.by-id.%s.%s %s" # MAC, metric, value

def get_mac():
    from network import WLAN
    from ubinascii import hexlify
    return hexlify(WLAN().config('mac'),'-').decode()

def carbon_client(server = "8.8.8.8", port = 2003, deepsleep = False, measure_n_send_cb = None, interval = INTERVAL):
    import gc
    import socket
    import time
    import network
    wifi = network.WLAN(network.STA_IF)

    while True:
        while not wifi.isconnected(): 
            print ("wait for wifi ...")
            sleep(ERROR_WAIT)
        print ("wifi.isconnected", wifi.isconnected())
        print ("wifi ", wifi.ifconfig())

        try:
            sock = socket.socket()
            sock.connect( socket.getaddrinfo(server, port)[0][-1] )

            if measure_n_send_cb != None:
                measure_n_send_cb(sock, send_cb)

            sock.close()
            sock = None
            gc.collect()

            sleep(interval, deepsleep)
        except Exception as e:
            print(e)
            sleep(ERROR_WAIT)

def send_cb(sock, metric, value):
    import gc

    mac = get_mac()
    m = METRIC_FMT % ( mac, metric, value)
    print(m)
    sock.write(m)
    sock.write(b'\n')
    m = None
    gc.collect()

def sleep(sec, deepsleep = False):
    if deepsleep:
        import machine
        rtc = machine.RTC()
        rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
        rtc.alarm(rtc.ALARM0, sec * 1000)
        print("deepsleep", sec, "s")
        machine.deepsleep()
    else:
        import time
        time.sleep(sec)

