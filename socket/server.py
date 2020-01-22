import socket
import sys
from select import select
import os
import pickle

class tcp_server:
    def __init__(self):
        u = open('/home/yoyojoejoe/桌面/socket/account.pkl' , 'rb')
        self.user = {}
        self.user = pickle.load(u, encoding='utf-8')
        self.userlist = []
        self.ip = "127.0.0.1"
        self.port = 999
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        u.close()
        
    def register(self, sock):
        sock.send('1'.encode('utf-8'))
        account = sock.recv(1024).decode('utf-8')
        sock.send('1'.encode('utf-8'))
        password = sock.recv(1024).decode('utf-8')
        if(self.user.setdefault(account, None)!=None):
            sock.send('Register failed.This account has been registered'.encode('utf-8'))
            return
        else:
            sock.send('Register sucess. Please restart this program'.encode('utf-8'))
            self.user[account]= password
            file = open('/home/yoyojoejoe/桌面/socket/account.pkl', 'wb')
            pickle.dump(self.user, file)
            file.close()
            return
    
    def validate(self, sock):
        data = sock.recv(1024).decode('utf-8')
        if(data == '1'):
            sock.send("1".encode('utf-8'))
            account = sock.recv(1024).decode('utf-8')
            sock.send("1".encode('utf-8'))
            password = sock.recv(1024).decode('utf-8')
            if(self.user.setdefault(account, None)!=None):
                if(self.user.setdefault(account, None) == password):
                    self.userlist.append(account)
                    sock.send("Wellcome to this chat room".encode('utf-8'))
                    return True
                else:
                    sock.send("Wrong password".encode('utf-8'))
                    return False
                    
            else:
                sock.send("The account hasn't been registered".encode('utf-8'))
                return False
        else:
            self.register(sock)
            return False

    def connect(self,sock):
        rlist = [sock, sys.stdin]
        while True:
            rs, _, _ = select(rlist, [], [])
            for r in rs:
                if (r is sock):
                    conn, addr = sock.accept()
                    if (self.validate(conn)):
                        rlist.append(conn)
                        print("Connect created from" + str(addr))
                    else:
                        conn.close()
                elif r is sys.stdin:
                    data = sys.stdin.readline()
                    data = "Administrator : " + data
                    for c in rlist[2:]:
                        c.send(data.encode('utf-8'))
                else:
                    data = r.recv(1024).decode('utf-8')
                    if (not data):
                        r.close()
                        rlist.remove(r)
                    else:
                        for c in rlist[2:]:
                            if (c is not r):
                                c.send(data.encode('utf-8'))

    def create(self):
        print("Server create sucessful")
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.ip, self.port))
        self.s.listen(100)
        self.connect(self.s)

def main():
    s = tcp_server()
    s.create()
main()