"""
Picarro Serial-UDP Transfer Script

This script is used to transfer the serial data from the Picarro gas analyzer over UDP to OpenRVDAS.

"""

import serial
import socket
import logging
import time
import datetime

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

logging.info("PICARRO SERIAL-UDP TRANSFER INITIATED")

# Setup socket for UDP transfer
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


# Setup serial port on Picarro
while True:

    try:

        ser = serial.Serial("COM2", 19200, timeout=5)
        break

    except serial.SerialException:

        logging.warning("No serial connection established: will try to connect in 10 seconds")
        time.sleep(10)


while True:

    try:

        s = ser.readline()

        if len(s) <= 1:

            logging.warning("No data currently available: will check again in 10 seconds")
            time.sleep(10)

        elif len(s) > 1:
            timestamp = datetime.datetime.now()
            s = str(timestamp) + ' ' + str(s)
            print(s)
            print("Sending UDP")
            sock.sendto(bytes(str(s), "utf-8"), ("255.255.255.255", 30330))
            print("Done")

    except KeyboardInterrupt:
        logging.error("Program stopped")
        break

    except Exception as e:
        logging.error("Exception occurred")
        break
