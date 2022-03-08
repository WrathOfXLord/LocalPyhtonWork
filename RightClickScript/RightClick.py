import time
import threading
from pynput import mouse
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delayRate = 1e-3
button = Button.right
startStopKey = KeyCode(char="e")
exitKey = KeyCode(char="q")

class MouseClick(threading.Thread):
    def __init__(self, delay, button):
        threading.Thread.__init__(self)
        self.delay = delay
        self.button = button
        self.isRunning = False
        self.isProgramRunning = True

    def startClicking(self):
        self.isRunning = True

    def stopClicking(self):
        self.isRunning = False

    def exit(self):
        self.stopClicking()
        self.isProgramRunning = False

    def run(self):
        while self.isProgramRunning:
            while(self.isRunning):
                mouse.click(self.button)
                time.sleep(self.delay)


print("program starts")
print("keycode for e: ", startStopKey)
print("keycode for q: ", exitKey)
mouse = Controller()
clickThread = MouseClick(delayRate, button)
clickThread.start()

def onPress(key):
    if key == startStopKey:
        if clickThread.isRunning:
            clickThread.stopClicking()
        else:
            clickThread.startClicking()
    elif key == exitKey:
        clickThread.exit()
        listener.stop()

with Listener(onPress) as listener:
    listener.join()