# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

import CONFIG

def get_mac():
    from network import WLAN
    from ubinascii import hexlify
    return hexlify(WLAN().config('mac'),'-').decode()

def sleep(sec, deepsleep = False):
    import time
    if deepsleep:
        import machine
        rtc = machine.RTC()
        rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
        rtc.alarm(rtc.ALARM0, sec * 1000)
        if CONFIG.DEBUG:
            print("sleep:", sec, "s (DEEP SLEEP)")
        machine.deepsleep()
        time.sleep_us(100)
    else:
        if CONFIG.DEBUG:
            print("sleep:", sec, "s")
        time.sleep(sec)

# vim: sw=4 ts=4 ft=python et foldmethod=indent
