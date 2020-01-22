import tkclient
import tkinter as tk
import os

class register:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('register')
        self.window.geometry('500x300')
        self.e1 = tk.Entry(self.window,width=30, show =None)
        self.e1.place(x=120,y=70)
        self.e2 = tk.Entry(self.window,width=30, show =None)
        self.e2.place(x=120,y=100) 
        self.account =''
        self.password = ''
        self.b = tk.Button(self.window, text='ok',  width=3, height=2, command=self.exe)
        self.b.place(x=400, y=70)
        self.t = tk.Text(self.window, height=1)
        self.t.place(y=150)
    def exe(self):
        self.account = self.e1.get()
        self.password = self.e2.get()
        c = tkclient.tcp_client(self.account, self.password, self.window, self.t)
        c.register()
    def mainloop(self):
        self.window.mainloop()

if __name__ == '__main__':
    a=register()
    a.mainloop()