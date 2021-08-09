from tkinter import *
from tkinter import messagebox
from pandas import *
from datetime import *
from numpy import *
import os
 
root = Tk()
root.title("Chat App")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(2,weight=1)
button1 = Button(root, text="Server")#,command = function)
button2 = Button(root, text="Client")
serverip = Label(root, text = "IP:")
serveripentry = Entry(root)
serveripentry.insert(INSERT,"127.0.0.1")
serverport = Label(root, text = "Port:")
serverportentry = Entry(root)
serverportentry.insert(INSERT,"1337 (already filled for srever , client fills this)")
serverstatus = Label(root, text = "Connected (connect button for client)")
# serverstatus.
chat = Text(root)
chat.insert(INSERT,"client : Hi\nserver : ok\nclient : ok\n")
chat.insert(INSERT,"client : Hi\nserver : ok\nclient : ok")
inputbox = Entry(root)
send = Button(root, text="Send")#,command = show)
button1.grid(row = 0, column = 0 , columnspan= 2, sticky = N+S+W+E, pady = 2)
button2.grid(row = 0, column = 2 ,columnspan= 2, sticky = N+S+W+E, pady = 2)
serverip.grid(row = 1, column = 0 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serveripentry.grid(row = 1, column = 1 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverport.grid(row = 1, column = 2 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverportentry.grid(row = 1, column = 3 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverstatus.grid(row = 1, column = 4 , columnspan= 1, sticky = N+S+W+E, pady = 2)
chat.grid(row = 2, column = 0, columnspan = 4 , sticky = N+S+E+W, pady = 2)
inputbox.grid(row = 3, column = 0, columnspan = 3 ,sticky = W+E, pady = 2)
send.grid(row = 3, column = 3, sticky = W+E, pady = 2)
root.mainloop()
