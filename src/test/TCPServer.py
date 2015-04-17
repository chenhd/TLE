#-*- coding: utf-8 -*-
'''
Created on 2014年12月7日

@author: Grey
'''

from socket import *
from time import ctime
import os

# UDPSocket = socket.socket(socket.AF_INET, SOCK_DGRAM)
# TCPSocket = socket.socket()
TCPServerSocket = socket(AF_INET, SOCK_STREAM)

HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

TCPServerSocket.bind(ADDR)
TCPServerSocket.listen(5)


while True:
    print 'waitting for connection...'
    TCPClientSocket, addr = TCPServerSocket.accept()
    print '...connected from:', addr
    time = 1
    goal = ''
    while True:
        data = TCPClientSocket.recv(BUFSIZ)
        if not data:
            break
        TCPClientSocket.send('[%s] %s' % (ctime(), data))
        goal = data
        
        print time
        time += 1
    file = open('./Testinput','a')

    file.write(ctime() + " : " + goal + '\n')

    file.close()
    TCPClientSocket.close()





