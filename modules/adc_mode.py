# set_adc_mode makes reading Vcc possible
#
# example:
#    import machine
#    vcc = machine.ADC(1)
#    vcc.read()
#
# See
#    https://github.com/micropython/micropython/issues/2352

# to enable Vcc read, execute once
#
# import adc_mode
# adc_mode.set(adc_mode.ADC_MODE_VCC)
#

ADC_MODE_VCC = 255
ADC_MODE_ADC = 0

def set(mode):
    import esp
    from flashbdev import bdev
    import machine

    sector_size = bdev.SEC_SIZE
    flash_size = esp.flash_size()
    init_sector = int(flash_size / sector_size - 4)
    data = bytearray(esp.flash_read(init_sector * sector_size, sector_size))
    if data[107] == mode:
        return  # flash is already correct; nothing to do
    else:
        data[107] = mode  # re-write flash
        esp.flash_erase(init_sector)
        esp.flash_write(init_sector * sector_size, data)
        print("ADC mode changed in flash; restart to use it!")
        return

# vim: sw=4 ts=4 ft=python et foldmethod=indent
