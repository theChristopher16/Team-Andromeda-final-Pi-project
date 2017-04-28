import RPi.GPIO as GPIO
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
import random
from time import sleep
import threading
import time

L = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",\
     "r","s","t","u","v","w","x","y","z"]
t = {}
t["a"] = "." + "_"
t["b"] = "_"+ "." + "." + "."
t["c"] = "_" + "." +"_" + "."
t["d"] = "_" +"." + "."
t["e"] = "."
t["f"] = "." + "." + "_" + "."
t["g"] = "_" + "_" +"."
t["h"] = "." +"." +"." +"."
t["i"] = "." + "." 
t["j"] = "." + "_" +"_" +"_"
t["k"] = "_" +"." +"_"
t["l"] = "." + "_" + "." + "."
t["m"] = "_" + "_"
t["n"] = "_" +"."
t["o"] = "_" +"_" +"_" 
t["p"] = "." +"_" +"_" + "."
t["q"] = "_" + "_" +"." +"_"
t["r"] = "." + "_" +"."
t["s"] = "." + "." + "."
t["t"] = "_"
t["u"] = "."+ "." +"_"
t["v"] = "." +"." +"." + "_"
t["w"] = "." + "_" +"_" 
t["x"] = "_" +"." +"." + "_" 
t["y"] = "_" + "." +"_" +"_"
t["z"] = "_" + "_"+"." +"." + "."

password = ""
for i in range (7):
    n = random.randint(0,25)
    password += "{}".format(L[n])
password2 = list(password)

print password2

def morse(x):
    return t[x]
password2 = [i.replace(i,morse(i))for i in password2]
print password2

def setGPIO():
    gpio = [4,17,27,22,5,6,13]
    for i in gpio:
        GPIO.setup(i, GPIO.OUT)
    return gpio

##def flash(n,x):
##    for i in password2[x]:
##        if i == ".":
##            GPIO.output(gpio[n],GPIO.HIGH)
##            sleep(0.4)
##            GPIO.output(gpio[n],GPIO.LOW)
##            sleep(1)
##            print 1
##        else:
##            GPIO.output(gpio[n],GPIO.HIGH)
##            sleep(1)
##            GPIO.output(gpio[n],GPIO.LOW)
##            sleep(0.5)
##            print 2
##def go():
##    for i in range(7):
##        flash(i,i)
##        time.sleep(0.0)
##        

class Mythread(threading.Thread):
    def __init__(self,n,x):
        threading.Thread.__init__(self)
        self.n = n
        self.x = x
        
        
    def run(self):
        GPIO.setmode(GPIO.BCM)
        for i in password2[self.x]:
            if i == ".":
                GPIO.output(gpio[self.n],GPIO.HIGH)
                sleep(0.05)
                GPIO.output(gpio[self.n],GPIO.LOW)
                sleep(0.1)
                
            else:
                GPIO.output(gpio[self.n],GPIO.HIGH)
                sleep(0.15)
                GPIO.output(gpio[self.n],GPIO.LOW)
                sleep(0.25)
                
        
        
def display():
    try:
    
        while(True):
            for x in range(7):
                mythread = Mythread(x,x)
                mythread.start()
                time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()

    
        


gpio = setGPIO()
global gpio
global password2
display()
raw_input("Press ENTER to terminate")


