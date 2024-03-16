from sys import argv
import tinytuya

if (len(argv) == 6):
    d = tinytuya.OutletDevice(dev_id=argv[1], address=argv[2], local_key=argv[3], version=float(argv[4]))
    d.turn_off() if argv[5].strip().lower() == 'off' else d.turn_on()