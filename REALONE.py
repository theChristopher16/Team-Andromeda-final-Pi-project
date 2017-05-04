import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import random
from Tkinter import *
import time
from time import sleep
from multiprocessing.pool import ThreadPool
from threading import Thread
import threading
import os
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
uname = "notreal"
def password():
    password = ""
    for i in range (7):
        n = random.randint(0,25)
        password += "{}".format(L[n])
    return password
def test():
    global pcheck
    pcheck  = 3

def func1(x):
    return (time.time()-(x))

def morse(x):
    return t[x]
def setGPIO():
    gpio = [4,17,27,22,5,6,13]
    for i in gpio:
        GPIO.setup(i, GPIO.OUT)
    return gpio
def display(r):
    
    while((time.time()-r)<10):
        for x in range(7):
           mythread = Mythread(x,x)
           mythread.start()
           time.sleep(1)
class Empty(Frame,Canvas):
    r = time.time()
    def __init__(self,master,parent):
        Canvas.__init__(self,master,bg = "white")
        Frame.__init__(self,parent)
        self.pack(fill = BOTH,expand = 1)

    def gui(self):
        self.pack(fill = BOTH, expand = 1)
        Empty.player_input = Entry(self,bg = "white")
        Empty.player_input.bind("<Return>", self.process)
        Empty.player_input.pack(side = BOTTOM, fill=X)
        Empty.player_input.focus()

        text_frame = Frame(self,width = 520/2)
        Empty.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Empty.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

        
        Empty.player_password = Label(self,text = "Enter your team name:  ")
        Empty.player_password.pack(side = BOTTOM)

    def setUS(self,status=""):
        Empty.text.config(state=NORMAL)
        Empty.text.delete("1.0",END)
        Empty.text.insert(END, "USERNAME: " + str(status))
        Empty.text.config(state = DISABLED)

    def setPS(self,status= ""):
        Empty.text.config(state=NORMAL)
        Empty.text.delete("2.0", "3.0")
        Empty.text.insert(END, "\nPASSWORD: " + str(status))
        Empty.text.config(state = DISABLED)


    def changeText(self,n):
        Empty.player_password.config(text = n)

    def process (self,event):
        name = Empty.player_input.get()
        name = name.lower()
        team = name.split()
        if (len(team) ==1):
            #print ((time.time()-r))
            tname = team[0]
            ur = "try again"
            pr = "try again"
            if  (tname in users):
                global uname
                uname = tname
                self.changeText("Enter Password: ")
                response = str(tname) + "192.168.2.6"
                pt = "Solve the password"
                self.setUS(response)
                self.setPS(pt)

            elif (tname == (pass1)):
                ps = pass2
                self.setPS(ps)
                test()
                
               
            else:
                self.setUS(ur)
                self.setPS(pr)


        
            Empty.player_input.delete(0, END)

class Mythread(threading.Thread):
    def __init__(self,n,x):
        threading.Thread.__init__(self)        
        self.x = x
        self.n = n
        
        
    def run(self):
        GPIO.setmode(GPIO.BCM)
        for i in mpass[self.x]:
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
                
def gui():
    window = Tk()
    global g
    g = Empty(window,window)
    g.gui()
    window.geometry("600x520")
    window.mainloop()

def input1(x):
    file = open("input13", "w+")
    file.truncate
    file.write(x+"\n")
    file.write(x)

    file.close

def run():
    p = 0
    x = time.time()
    sleep(2)
    while (p < 5):
        p1 = pool.apply_async(func1,(x,))
        p = p1.get()
def input1(n):
    f = open("input13", "w+")
    deleteContent(f)
    f.write(pass2+"\n")
    f.write(pass2)

    file.close
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

users = ["notreal","red","yellow"]
g = 0
pass1 = password()
mpass = [i.replace(i,morse(i))for i in pass1]
pass2 = password()  
pcheck = 2
pool = ThreadPool(processes = 1)
button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

MATT = 15
gpio = setGPIO()
for i in users:
    os.system("sudo userdel -r " +i)
for i in users:
    os.system("sudo adduser " + i + "<input13")
while (MATT == 15):
    if (GPIO.input(button) == GPIO.LOW):
        Thread(target = gui).start()
        while (pcheck == 2):
            x = time.time()

            
            pass1 = password()
            mpass = [i.replace(i,morse(i))for i in pass1]
            pass2 = password()
            print pass1
            print mpass
            print pass2
            input1(pass2)
            #os.system("sudo passwd " + uname + "<input1")
            print uname
            display(x)
            print pass2
        os.system("sudo passwd " + uname + "<input13")
        MATT = 14
        
print "REACHED THE END"
