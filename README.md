# iot-carbon - ESP Temperature sensor with MicroPython using Carbon

This is a very simple implementation of a sensor reader, which submits
afterwards to a carbon server.

An example module for BME280 sensors is included.

The scripts might easily be adapted to other Micropython based boards.

## Uploading to your ESP board

All scripts assume that MicroPython is already installed and a USB to serial
converter is connected to the ESP as /dev/ttyUSB0.

* `up.sh`, uploads all .py scripts to the ESP

### External tools used

There some shell scripts that make deloyment of the Python scripts easier.
These tools are needed:

 * [mpfshell](https://github.com/wendlers/mpfshell)
 * [rshell](https://github.com/dhylands/rshell)

### We have not time, what is the clock?

If you have an carbon server that does not accept metrics without Epoch,
you need carbon relay that is augmenting the metrics.
 * [carbuffd](https://github.com/j0ju/carbuffd)

## QuickStart

Install mpfshell and rshell to your computer, either via your
distributions/os package manager or via `pip` to a virtual env.
 * Install .py-files from `./modules` using `up.sh`
 * Install .py-files from `./`
 * Install or adapt a `main.py` from a directory below `./examples`

As ESP boards does not have a reliable battery buffered RTC, it was choosen
not to send Epochs (seconds since 1970 @ GMT) in the carbon metrics.
Install and run carbuffd.

## Vcc measurement

To measure the voltage Vcc the firmware has to be patched, see `./modules/adc_mode.py`.

