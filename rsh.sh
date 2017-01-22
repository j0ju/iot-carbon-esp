#!/bin/sh

DEV=ttyUSB0
[ -f .port ] && . ./.port
export RSHELL_PORT="/dev/$DEV"

exec rshell

