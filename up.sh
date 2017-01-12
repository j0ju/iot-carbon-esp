DEV=ttyUSB0
export RSHELL_PORT="/dev/$DEV"

(
  echo "open ttyUSB0"
  for py in *.py; do
    echo "put $py"
  done
  echo "ls"
) | \
 mpfshell --nocolor --nocache

rshell repl '~ import machine; machine.reset() ~'

