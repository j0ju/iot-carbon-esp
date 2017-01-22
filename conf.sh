#!/bin/sh
# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

DEV=ttyUSB0
[ -f .port ] && . ./.port
export RSHELL_PORT="/dev/$DEV"

(
  echo "open $DEV"
  for py in main.py CONFIG.py; do
    echo "put $py"
    echo $py >&2
  done
  echo "ls"
) | \
  mpfshell --nocolor --nocache

