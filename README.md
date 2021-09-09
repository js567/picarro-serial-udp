# picarro-serial-udp
Simple script for transferring serial data from Picarro gas composition sensor over UDP

## To set up for RCRV:

1. Attach a null modem 9-pin serial cable to the back of the Picarro analyzer between the COM1 and COM2 ports
2. Start the picarro_serial_udp.py to confirm that the program is properly collecting data

FOR AUTOMATIC STARTUP
1. Run the included .exe file and start it to ensure it has the same output as the .py file
   (the .py file will need to be stopped so that the serial port is free)
2. In file explorer, navigate to C:\Users\username\Appdata\Roaming\Microsoft\Start Menu\Programs\Startup
3. Place the .exe file in the Startup folder
4. Restart the machine to ensure that data is collected and transferred properly 

TO EDIT AUTOMATIC STARTUP FILE
1. Remove file from Startup folder
2. pip install pyinstaller
3. Edit .py file 
4. pyinstaller picarro_serial_udp.py
5. .exe file can be found in 'dist' folder in same directory
