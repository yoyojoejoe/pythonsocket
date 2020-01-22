import socket
import sys
from select import select
import threading
import os
import pickle

class tcp_client:
    def __init__(self, account, password):
        self.ip = '127.0.0.1'
        self.port = 999
        self.account = account
        self.password = password
        self.kick = ''
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def register(self, account, password, sock):
        sock.connect((self.ip, self.port))
        sock.send("2".encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        sock.send(account.encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        sock.send(password.encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        if(data == 'Register sucess. Please restart this program'):
            print(data)
            return True
        else:
            print(data)
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
            print(data)
            data = self.account + '  join the chatroom' + '\n'
            sock.send(data.encode('utf-8'))            
            return True
        else:
            print(data)
            return False
        
    def send_msg(self,sock):
        while True:
            data = input()
            if (data =="exit()"):
                data = self.account + "leave the chat room"
                sock.send(data.encode('utf-8'))
                sock.close()
                os._exit(0)
            else:
                data = self.account + ':' + data
                sock.send(data.encode('utf-8'))
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
                print(data)
    def connect(self):
        if(self.login(self.s)):
            threading.Thread(target=self.send_msg, args=(self.s,)).start()
            threading.Thread(target=self.recv_msg, args=(self.s,)).start()

def main():
    account = input("account:")
    password = input("password:")
    c = tcp_client(account, password)
    c.connect()
    
if __name__ == '__main__':
    main()   