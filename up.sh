#!/bin/sh
# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

DEV=ttyUSB0
[ -f .port ] && \
    . ./.port
export RSHELL_PORT="/dev/$DEV"

FORCE=no
if [ "$1" = -f ]; then
    FORCE=yes
    shift
fi

if ! [ "$#" = 0 ]; then
    FORCE=yes
fi

(   echo "open $DEV"
    for py in ${*:-*.py}; do
        echo "put $py"
        echo "up $py" >&2
    done
    echo "ls"
) | \
    mpfshell --nocolor --nocache

echo
# vim: ft=sh sw=4 ts=4 et
