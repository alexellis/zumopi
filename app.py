from motors import *
from wiimote import *
import os
import sys

def go():
    remote = Wiimote()
    remote.connect()
    remote.rumble(0.50)

    motors1 = motors()
    while(True):
        command = remote.read_command()
#        print(command)

        vals = ["U","D","L","R"]

        found = None
        for val in vals:
            if command.has_key(val):
                found = val
        if(found !=None):
            motors1.drive(found)
        elif(command.has_key("HOME")):
            remote.rumble(0.50)
            os.system("shutdown -h 0");
            sys.exit()
        else:
            motors1.stop()
        time.sleep(0.10)

go()

