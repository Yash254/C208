#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name=None
listbox=None
textarea=None
labelchat=None
text_message=None

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    openChatWindow()

def openChatWindow():
    window=Tk()
    window.title('Messenger')
    window.geometry('500x350')

    namelabel=Label(window,text='Enter your name', font=('Calibri', 10))
    namelabel.place(x=10, y=8)
    
    name=Entry(window, width=30, font=('Calibri', 10))
    name.place(x=120, y=8)
    name.focus()

    connectServer=Button(window, text='connect to chat server', bd=1, font=('Calibri', 10))
    connectServer.place(x=360, y=6)
    
    seperator=ttk.Separator(window, orient='horizontal')
    seperator.place(x=0, y=35, relwidth=1, height=0.1)
    
    connectButton=Button(window, text='connect', bd=1, font=('Calibri', 10))
    connectButton.place(x=282, y=160)

    disconnectButton=Button(window, text='disconnect', bd=1, font=('Calibri', 10))
    disconnectButton.place(x=350, y=160)

    refresh=Button(window, text='refresh', bd=1, font=('Calibri', 10))
    refresh.place(x=435, y=160)

    labelchat=Label(window, text='Chat Window', font=('Calibri', 10))
    labelchat.place(x=10, y=180)
    
    textarea=Text(window, width=67, height=6, font=('Calibri', 10))
    textarea.place(x=10, y=200)

    scrollbar2=Scrollbar(textarea)
    scrollbar2.place(relheight=1, relx=1)
    # scrollbar2.config(command=listbox.yview)
    
    text_message=Entry(window, width=43, font=('Calibri', 10))
    text_message.place(x=98, y=306)
    text_message.pack()

    send=Button(window, text='send', bd=1, font=('Calibri', 10))
    send.place(x=450, y=305)

    filePathLabel=Label(window, text='', font=('Calibri', 10), fg='blue')
    filePathLabel.place(x=10, y=330)



    window.mainloop()

setup()

#-----------Bolierplate Code Start -----