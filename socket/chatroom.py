import tkinter as tk
import tkclient

class chat_room:
    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.window = tk.Tk()
        self.window.title('chat room')
        self.window.geometry('500x700') 
        self.t = tk.Text(self.window, height=34)
        self.e1 = tk.Entry(self.window,width=50, show =None)
        self.t.pack()
        self.e1.place(y=600)
        self.b1 = tk.Button(self.window, width=10,height=2)
        self.c = tkclient.tcp_client(account, password, self.window, self.t, self.e1, self.b1) 
        self.c.connect()
        self.b1= tk.Button(self.window,text='send', width=3,height=1,command=self.c.send_msg)
        self.b1.place(x=420,y=600)
    def exe(self):  
        self.window.mainloop()
