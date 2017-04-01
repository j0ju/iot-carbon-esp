# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

METRIC_FMT = b'iot.by-id.%s.%s %s' # MAC, metric, value

def client( server = '203.0.113.1',
            port = 2003,
            RETRIES = 3, ERROR_WAIT = 1 ):
    import network
    import time
    wifi = network.WLAN(network.STA_IF)

    while not wifi.isconnected():
        print (b'wifi: waiting for ...')
        time.sleep(ERROR_WAIT)
        print (b'wifi.isconnected: ', wifi.isconnected())
        print (b'wifi: ', wifi.ifconfig())

    import socket
    for i in range(1, RETRIES):
        try:
            s = socket.socket()
            s.connect( socket.getaddrinfo(server, port)[0][-1] )
            print (b'connected: ', server, b' port', port, b'(try', i, b')')
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
    m = METRIC_FMT % ( mac, metric, value )
    print('send: ', m)
    sock.write(m)
    sock.write(b'\n')
    m = None

    import gc
    gc.collect()

# vim: sw=4 ts=4 ft=python et foldmethod=indent
