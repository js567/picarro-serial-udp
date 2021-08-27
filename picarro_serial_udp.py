import serial
#import serial.tools.list_ports
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

ser = serial.Serial("COM2", 19200, timeout=5)

while True:

    try:

        s = ser.readline()
        print(s)
        print("Sending UDP")
        sock.sendto(bytes(str(s), "utf-8"), ("255.255.255.255", 30330))
        print("Done")

    except Exception:
        break
