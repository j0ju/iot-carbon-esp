#!/bin/sh
# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

DEV=ttyUSB0
[ -f .port ] && . ./.port
export RSHELL_PORT="/dev/$DEV"

exec rshell

