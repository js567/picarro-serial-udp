import serial
import serial.tools.list_ports
import socket

ser = serial.Serial()

print(list(serial.tools.list_ports.comports()))
print('hello')