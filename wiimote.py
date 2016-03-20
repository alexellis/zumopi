import cwiid
import time

class Wiimote:
    def connect(self):
        wii=cwiid.Wiimote()
        wii.rpt_mode = cwiid.RPT_BTN
        self.wii=wii

    def rumble(self, duration):
        self.wii.rumble = True
        time.sleep(duration)
        self.wii.rumble = False

    def read_command(self):    
        states = {}
        buttons = self.wii.state['buttons']
        if buttons & cwiid.BTN_A:
            states["A"] = True
        if buttons & cwiid.BTN_B:
            states["B"]=True
        if buttons & cwiid.BTN_LEFT:
            states["L"] = True
        if buttons & cwiid.BTN_RIGHT:
            states["R"] = True
        if buttons & cwiid.BTN_UP:
            states["U"] = True
        if buttons & cwiid.BTN_DOWN:
            states["D"] = True
        if buttons & cwiid.BTN_HOME:
            states["HOME"] = True
        return states

if(__name__ == '__main__'):
    remote = Wiimote()
    remote.connect()
    while(True):
        command = remote.read_command()
        print(command)
        time.sleep(0.15)
