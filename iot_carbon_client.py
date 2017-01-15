# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

INTERVAL = 45
ERROR_WAIT = 1
METRIC_FMT = "iot.by-id.%s.%s %s" # MAC, metric, value
RETRIES = 3

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
            print ("wifi: waiting for ...")
            sleep(ERROR_WAIT)
        print ("wifi.isconnected: ", wifi.isconnected())
        print ("wifi: ", wifi.ifconfig())

        for i in range(1, RETRIES):
            try:
                sock = socket.socket()
                sock.connect( socket.getaddrinfo(server, port)[0][-1] )

                if measure_n_send_cb != None:
                    measure_n_send_cb(sock, send_cb)

                sock.close()
                sock = None
                gc.collect()
                
                print("connection succeded: try", i)
                break

            except Exception as e:
                print("sending failed:", e)
                sleep(ERROR_WAIT)
        
        sleep(interval, deepsleep)

def send_cb(sock, metric, value):
    import gc

    mac = get_mac()
    m = METRIC_FMT % ( mac, metric, value)
    print("send: ", m)
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
        print("sleep:", sec, "s (DEEP SLEEP)")
        machine.deepsleep()
        time.sleep_us(100)
    else:
        import time
        print("sleep:", sec, "s")
        time.sleep(sec)

# vim: sw=4 ts=4 ft=python et
