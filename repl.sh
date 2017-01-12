DEV=ttyUSB0
export RSHELL_PORT="/dev/$DEV"

exec rshell repl

