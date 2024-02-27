import tinytuya
from sys import argv, exit

if (len(argv) < 5):
    exit()

d = tinytuya.OutletDevice(argv[1], argv[2], argv[3])
d.set_version(float(argv[4]))

if argv[5].strip().lower() == 'on':
    d.turn_on()
else:
    d.turn_off()