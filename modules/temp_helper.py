# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

# reference: http://en.wikipedia.org/wiki/Dew_point
# delta max = 0.6544 wrt dewPoint()
def dew_point(celsius, humidity):
    from math import log

    a = 17.271
    b = 237.7
    temp = (a * celsius) / (b + celsius) + log(humidity*0.01)
    return (b * temp) / (a - temp);

# vim: sw=4 ts=4 ft=python et foldmethod=indent
