import bluetooth
import socket

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

xm = '00:11:35:57:61:30'

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))
    if addr == xm:
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.connect((xm, 4))
        s_sock = s.accept()
        print("Accepted connection with xm")