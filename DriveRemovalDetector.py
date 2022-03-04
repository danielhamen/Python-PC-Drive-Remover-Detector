import win32api
import time
from termcolor import colored

def onDisconnect():
    return (colored(f"Drive disconnected ", "red"))

def onConnect():
    return (colored(f"Drive is connected ", "green"))

class DriveRemovalDetector:
    def __init__(self, Target, Iterations=10, CheckIntervals=0.1, onDisconnect=onDisconnect(), onConnect=onConnect()):
        self.Target = str(Target)
        self.Drives = []
        self.CheckIntervals = float(CheckIntervals)
        self.Iterations = int(Iterations)
        self.onDisconnect = onDisconnect
        self.onConnect = onConnect

    def DetectDrives(self):
        Drives = win32api.GetLogicalDriveStrings()
        Drives = str(Drives).split("\000")
        NewDrives = []
        for Drive in Drives:
            Drive = str(Drive).replace(":\\", "")
            NewDrives.append(Drive)
        self.Drives = NewDrives[:-1]

    def Start(self):
        for LoopIndex in range(0, self.Iterations):
            self.DetectDrives()
            self.Target = self.Target.replace(":\\", "")
            if self.Target in self.Drives:
                print(self.onConnect)
            else:
                print(self.onDisconnect)
                exit()
            time.sleep(self.CheckIntervals)
