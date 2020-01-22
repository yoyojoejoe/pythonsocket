import tkinter as tk
import os
import chatroom
import register
account = ''
password = ''


window = tk.Tk()
window.title('client')
window.geometry('500x700')

e1 = tk.Entry(window, show =None)
e2 = tk.Entry(window, show = '*')
e1.place(x=160, y=250)
e2.place(x=160, y=280)
l1 = tk.Label(window, text='Account', font=('Arial', 12), width=10, height=1)
l2 = tk.Label(window, text='password', font=('Arial', 12), width=10, height=1)
l1.place(x=50,y=250)
l2.place(x=50,y=280)

def login():
    global account, password
    account = e1.get()
    password = e2.get()
    c = chatroom.chat_room(account,password)
    window.destroy()
    c.exe()
    
def mregister():
    r = register.register()
    window.destroy()
    r.mainloop()
b = tk.Button(window, text="login", width=5, height=2,command=login)
b.place(x=340, y=250)
b2 = tk.Button(window, text="register", width=5, height=2,command=mregister)
b2.place(x=420,y=250)
window.mainloop()