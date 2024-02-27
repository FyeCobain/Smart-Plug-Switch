from sys import argv, exit
import tinytuya

if (len(argv) < 5):
    exit()

d = tinytuya.OutletDevice(argv[1], argv[2], argv[3])
d.set_version(float(argv[4]))
d.turn_on() if argv[5].strip().lower() == 'on' else d.turn_off()