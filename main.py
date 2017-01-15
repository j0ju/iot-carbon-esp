# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

import machine
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('sleep: awoke from DEEP SLEEP')

import iot_dht22
iot_dht22.client(interval = 45, deepsleep = True)

# vim: sw=4 ts=4 ft=python et
