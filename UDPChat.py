from tkinter import *
from tkinter import messagebox
from pandas import *
from datetime import *
from numpy import *
from socket import *
import threading
from random import randint
import os
# s = None
port = randint(1024,65535)
name = "test"
def server():
    global s
    s = socket(AF_INET , SOCK_DGRAM )
    # s.bind(('',int(serverportentry.get())))
    s.bind(('',port))
    print("started")
    x2.start()
def send():
    message = "{}  : {}".format(name,inputbox.get())
    inputbox.delete(0,END)
    s.sendto(message.encode() , (serveripentry.get(),int(serverportentry.get())))

def rec():
    while True:
        msg = s.recvfrom(1024)
        chat.insert(INSERT,msg[0].decode() + "\n")
x2 = threading.Thread( target = rec)

root = Tk()
root.title("Chat App (127.0.0.1:" + str(port) + ")")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(2,weight=1)
button1 = Button(root, text="Start Server",command = server)
# button2 = Button(root, text="Client",command = client)
serverip = Label(root, text = "IP:")
serveripentry = Entry(root)
serveripentry.insert(INSERT,"127.0.0.1")
serverport = Label(root, text = "Port:")
serverportentry = Entry(root)
# serverportentry.insert(INSERT,"1337")
serverstatus = Label(root, text = "Connected ?")
chat = Text(root)
# chat.insert(INSERT,"client : Hi\nserver : ok\nclient : ok\n")
# chat.insert(INSERT,"client : Hi\nserver : ok\nclient : ok")
inputbox = Entry(root)
send = Button(root, text="Send",command = send)
button1.grid(row = 0, column = 0 , columnspan= 2, sticky = N+S+W+E, pady = 2)
# button2.grid(row = 0, column = 2 ,columnspan= 2, sticky = N+S+W+E, pady = 2)
serverip.grid(row = 1, column = 0 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serveripentry.grid(row = 1, column = 1 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverport.grid(row = 1, column = 2 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverportentry.grid(row = 1, column = 3 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverstatus.grid(row = 1, column = 4 , columnspan= 1, sticky = N+S+W+E, pady = 2)
chat.grid(row = 2, column = 0, columnspan = 4 , sticky = N+S+E+W, pady = 2)
inputbox.grid(row = 3, column = 0, columnspan = 3 ,sticky = W+E, pady = 2)
send.grid(row = 3, column = 3, sticky = W+E, pady = 2)
root.mainloop()
