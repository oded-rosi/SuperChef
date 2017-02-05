from xmodem import XMODEM


crc = xmodem.calc_crc('hello')
print crc