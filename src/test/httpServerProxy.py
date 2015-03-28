from socket import *
import time


# setdefaulttimeout(10)

def Proxy():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('127.0.0.1', 8070))
    s.listen(5)
    

    while True:
        sock, addr = s.accept()
        print '-' * 20, sock, addr
        time.sleep(0.1)
        send_data = sock.recv(4096)
        if not send_data:
            print 'send empty data'
            print '*' * 50
            continue
        time.sleep(0.1)
        
        
        
        
        s2 = socket(AF_INET, SOCK_STREAM)
        s2.connect(('127.0.0.1', 8080))
        s2.send(send_data)
        print 'send data :\n', send_data
        print '*' * 50
        time.sleep(0.1)
        rece_data = s2.recv(4096)
        time.sleep(0.1)
        sock.send(rece_data)
        time.sleep(0.1)
        print 'receive data :\n', rece_data
        print '*' * 50
        
        sock.close()
        s2.close()


if __name__ == '__main__':
    print 'start http server proxy ...'
    Proxy()




