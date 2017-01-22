# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

import CONFIG

def client(server = "203.0.113.1", port = 2003, RETRIES = CONFIG.RETRIES, ERROR_WAIT = CONFIG.ERROR_WAIT):
    import network
    import time
    wifi = network.WLAN(network.STA_IF)

    while not wifi.isconnected(): 
        if CONFIG.DEBUG:
            print ("wifi: waiting for ...")
        time.sleep(ERROR_WAIT)
    if CONFIG.DEBUG:
        print ("wifi.isconnected: ", wifi.isconnected())
        print ("wifi: ", wifi.ifconfig())

    import socket
    for i in range(1, RETRIES):
        try:
            s = socket.socket()
            s.connect( socket.getaddrinfo(server, port)[0][-1] )
            if CONFIG.DEBUG:
                print ("connected: ", server, " port", port, "(try", i, ")")
            break
        except Exception as e:
            s = None
            time.sleep(ERROR_WAIT)

    import gc
    gc.collect()

    return s

def send(sock, metric, value):
    from iot import get_mac

    mac = get_mac()
    m = CONFIG.METRIC_FMT % ( mac, metric, value )
    if CONFIG.DEBUG:
        print("send: ", m)
    sock.write(m)
    sock.write(b'\n')
    m = None

    import gc
    gc.collect()

# vim: sw=4 ts=4 ft=python et foldmethod=indent
