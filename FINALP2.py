import random
import os
from Tkinter import *
from threading import Thread
import time



L = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",\
     "r","s","t","u","v","w","x","y","z"]
c7 = {}
c10 = {}
c14 = {}
users = ["red","noname"]
d = [7,10]
usersd = {7: c7, 10: c10}
c7["a"] ="h"
c7["b"] ="i"
c7["c"] ="j"
c7["d"] ="k"
c7["e"] ="l"
c7["f"] ="m"
c7["g"] ="n"
c7["h"] ="o"
c7["i"] ="p"
c7["j"] ="q"
c7["k"] ="r"
c7["l"] ="s"
c7["m"] ="t"
c7["n"] ="u"
c7["o"] ="v"
c7["p"] ="w"
c7["q"] ="x"
c7["r"] ="y"
c7["s"] ="z"
c7["t"] ="a" 
c7["u"] ="b"
c7["v"] ="c"
c7["w"] ="d" 
c7["x"] ="e"
c7["y"] ="f" 
c7["z"] ="g"

c10["a"] ="k"
c10["b"] ="l"
c10["c"] ="m"
c10["d"] ="n"
c10["e"] ="o"
c10["f"] ="p"
c10["g"] ="q"
c10["h"] ="r"
c10["i"] ="s"
c10["j"] ="t"
c10["k"] ="u"
c10["l"] ="v"
c10["m"] ="w"
c10["n"] ="x"
c10["o"] ="y"
c10["p"] ="z"
c10["q"] ="a"
c10["r"] ="b"
c10["s"] ="c"
c10["t"] ="d"
c10["u"] ="e" 
c10["v"] ="f"
c10["w"] ="g" 
c10["x"] ="h" 
c10["y"] ="i" 
c10["z"] ="j"

c14["a"] ="o"
c14["b"] ="p"
c14["c"] ="q"
c14["d"] ="r"
c14["e"] ="s"
c14["f"] ="t"
c14["g"] ="u"
c14["h"] ="v"
c14["i"] ="w"
c14["j"] ="x"
c14["k"] ="y"
c14["l"] ="z"
c14["m"] ="a"
c14["n"] ="b"
c14["o"] ="c"
c14["p"] ="d"
c14["q"] ="e"
c14["r"] ="f"
c14["s"] ="g"
c14["t"] ="h" 
c14["u"] ="i"
c14["v"] ="j" 
c14["w"] ="k" 
c14["x"] ="l" 
c14["y"] ="m" 
c14["z"] ="n" 
def end():
    global sloop
    sloop = 1
class Empty1(Frame,Canvas):
    def __init__(self,master,parent):
        Canvas.__init__(self,master,bg = "white")
        Frame.__init__(self,parent)
        self.pack(fill = BOTH,expand = 1)

    def gui(self):
        self.pack(fill = BOTH, expand = 1)
        Empty1.player_input = Entry(self,bg = "white")
        Empty1.player_input.bind("<Return>", self.process)
        Empty1.player_input.pack(side = BOTTOM, fill=X)
        Empty1.player_input.focus()

        text_frame = Frame(self,width = 520/2)
        Empty1.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Empty1.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

        
        Empty1.player_password = Label(self,text = "Enter your team name:  ")
        Empty1.player_password.pack(side = BOTTOM)
        Empty1.text.insert(END,"Eu tu, Brutus")

    def setUS(self,status=""):
        Empty1.text.config(state=NORMAL)
        Empty1.text.delete("1.0",END)
        Empty1.text.insert(END, "Eu tu, Brutus \n" + status )
        Empty1.text.config(state = DISABLED)

    def end():
        sloop = 1
    def changeText(self,n):
        Empty1.player_password.config(text = n)

    def process (self,event):
        name = Empty1.player_input.get()
        name = name.lower()
        team = name.split()
        if (len(team) ==1):
            
            tname = team[0]
            ur = "try again"
            if  (tname in users):
                global uname
                name = tname
                self.changeText("Enter Password: ")
                pt = "Solve the password"
                self.setUS(pt)

            elif (tname == (password1)):
                global passcheck
                print" YOU SOLVED IT"
                passcheck = 1
                end()
            else:
                self.setUS(ur)


            Empty1.player_input.delete(0, END)
def func1(x):
    return (time.time()-(x))
           
        
def gui1():
    window = Tk()
    g = Empty1(window,window)
    g.gui()
    window.geometry("600x520")
    window.mainloop()
def password():
    password = ""
    for i in range (7):
        n = random.randint(0,25)
        password += "{}".format(L[n])
    return password
def morse(t,x):
    return t[x]
def wait():
    x = time.time()
    while (func1(x) < 16):
        if (passcheck == 1):
            p = 600
def input1(n):
    f = open("/home/pi/python_games/input1", "w+")
    deleteContent(f)
    f.write(n+"\n")
    f.write(n)
    f.close
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()


g = 0
passcheck = 0
Thread(target = gui1).start()
loop =2
sloop = 2
name = "red"
while(loop == 2):
    if name in users:
        t = random.choice(d)
        t = usersd[t]
        while (sloop == 2):
            password1 = password()
            password2 = [i.replace(i,morse(t,i))for i in password1]
            password2 = "".join(password2)
            input1(password2)
            os.system("sudo cp -r /home/pi/python_games/input1 /home/" + name + "/DESKTOP")
            print password1
            print password2
            wait()
        loop =1
print password1
print password2
print t
print "DONE"
