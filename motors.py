import explorerhat

class motors:
    def drive(self, dir):
        if(dir=="U"):
            explorerhat.motor.one.forwards()
            explorerhat.motor.two.forwards()
        elif(dir=="D"):
            explorerhat.motor.one.backwards()
            explorerhat.motor.two.backwards()
        elif(dir=="L"):
            explorerhat.motor.one.forwards()
            explorerhat.motor.two.backwards()
        elif(dir=="R"):
            explorerhat.motor.one.backwards()
            explorerhat.motor.two.forwards()

    def stop(self):
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
