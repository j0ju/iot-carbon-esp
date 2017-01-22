# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

METRIC_FMT = "iot.by-id.%s.%s %s" # MAC, metric, value

def client(server = "203.0.113.1", port = 2003, RETRIES = 3, ERROR_WAIT = 1):
    import network
    import time
    wifi = network.WLAN(network.STA_IF)

    while not wifi.isconnected(): 
        print ("wifi: waiting for ...")
        time.sleep(ERROR_WAIT)
    print ("wifi.isconnected: ", wifi.isconnected())
    print ("wifi: ", wifi.ifconfig())

    import socket
    for i in range(1, RETRIES):
        try:
            s = socket.socket()
            s.connect( socket.getaddrinfo(server, port)[0][-1] )
            print ("connected: ", server, " port", port, "(try", i, ")")
            break
        except Exception as e:
            s = None
            time.sleep(ERROR_WAIT)
    
    return s

def send(sock, metric, value):
    from iot import get_mac

    mac = get_mac()
    m = METRIC_FMT % ( mac, metric, value)
    print("send: ", m)
    sock.write(m)
    sock.write(b'\n')
    m = None

# vim: sw=4 ts=4 ft=python et foldmethod=indent
