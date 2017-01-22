#!/bin/sh

DEV=ttyUSB0
[ -f .port ] && . ./.port
export RSHELL_PORT="/dev/$DEV"

(
  echo "open $DEV"
  for py in *.py; do
    echo "put $py"
  done
  echo "ls"
) | \
  mpfshell --nocolor --nocache

