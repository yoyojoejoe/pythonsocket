import socket
import sys
from select import select
import threading
import os
import pickle
import tkinter as tk


class tcp_client:
    def __init__(self, account, password, window, text, entry=None, button=None):
        self.ip = '127.0.0.1'
        self.port = 999
        self.account = account
        self.password = password
        self.kick = ''
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.window = window
        self.text = text
        self.entry = entry
        self.button = button
        
    def register(self):
        self.s.connect((self.ip, self.port))
        self.s.send("2".encode('utf-8'))
        data = self.s.recv(1024).decode('utf-8')
        self.s.send(self.account.encode('utf-8'))
        data = self.s.recv(1024).decode('utf-8')
        self.s.send(self.password.encode('utf-8'))
        data = self.s.recv(1024).decode('utf-8')
        if(data == 'Register sucess. Please restart this program'):
            self.text.insert('end', data)
            self.text.insert('end', '\n')
            return True
        else:
            self.text.insert('end', data)
            self.text.insert('end', '\n')
            return False
                 
    def login(self, sock):
        sock.connect((self.ip, self.port))
        sock.send("1".encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        sock.send(self.account.encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        sock.send(self.password.encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        if (data == "Wellcome to this chat room"):
            self.kick = "Administrator : kick " + self.account + '\n'
            self.text.insert('end', data)
            self.text.insert('end', '\n')
            data = self.account + '  join the chatroom' + '\n'
            sock.send(data.encode('utf-8'))            
            return True
        else:
            self.text.insert('end', data)
            self.text.insert('end', '\n')
            return False
        
    def send_msg(self):
        data = self.entry.get()
        self.entry.delete('0','end')
        if (data =="exit()"):
            data = self.account + "leave the chat room"
            self.s.send(data.encode('utf-8'))
            self.s.close()
            os._exit(0)
        else:
            data = self.account + ':' + data
            self.s.send(data.encode('utf-8'))
    def recv_msg(self,sock):
        while True:
            data = sock.recv(1024).decode('utf-8')
            if(data == self.kick):
                data = "Administrator kick" + self.account
                sock.send(data.encode('utf-8'))
                sock.close()
                os._exit(0)
                break
            else:
                self.text.insert('end', data)
                self.text.insert('end', '\n')
    def connect(self):
        if(self.login(self.s)):
            threading.Thread(target=self.recv_msg, args=(self.s,)).start()

def main():
    account = input("account:")
    password = input("password:")
    c = tcp_client(account, password)
    c.connect()
    
if __name__ == '__main__':
    main()   