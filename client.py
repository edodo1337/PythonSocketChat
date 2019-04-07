import socket
import threading
import time

SERVER_ADDRES = ('localhost', 8356)


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(''), 'utf-8'))
            time.sleep(0.5)

    def __init__(self):
        self.sock.connect(SERVER_ADDRES)
        cThread = threading.Thread(target=self.sendMsg)
        cThread.demon = True
        cThread.start()
        while True:
            print('Client is running')
            time.sleep(0.5)
            try:
                data = self.sock.recv(1024)
                #print('\n')
                print(data.decode())
            except:
                print('error')
            finally:
                pass





client = Client()
