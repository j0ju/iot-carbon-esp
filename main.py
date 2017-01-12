# vim: sw=4 ts=4 ft=python et

#import esp
#esp.osdebug(None)

import iot_dht22
iot_dht22.client(interval = 30, deepsleep = False)

