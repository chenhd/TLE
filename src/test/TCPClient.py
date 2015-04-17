#-*- coding: utf-8 -*-
'''
Created on 2014年12月7日

@author: Grey
'''

from socket import *

HOST = 'localhost'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

TCPClientSocket = socket(AF_INET, SOCK_STREAM)
TCPClientSocket.connect(ADDR)


data = raw_input('please input any message: ')
if not data:
    print 'end !'
else:
    TCPClientSocket.send(data)
    
    data = TCPClientSocket.recv(BUFSIZ)
    if not data:
        print "doesn't receive the message !"
        print data
    
TCPClientSocket.close()
    



