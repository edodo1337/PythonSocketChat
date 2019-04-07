
import socket
import time
import threading


SERVER_ADDR = ('localhost', 8356)

class Server:
    connections = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):
        self.sock.bind(SERVER_ADDR)
        self.sock.listen(1)

    def handler(self, conn, addr):
        while True:
            try:
                data = conn.recv(1024)
                print(f"Message from {addr[0]}:{addr[1]}: {data.decode()}")
            except:
                print(f"Client: {addr[0]}:{addr[1]} disconnected")
                self.connections.remove(conn)
                conn.close()
                break
            for connection in self.connections:
                #print('Sending message...')
                if connection == conn:
                    #frm = bytes(str(addr[0])+':'+str(addr[1]))
                    connection.send(bytes('You:', encoding='utf-8')+bytes(data))
                else:
                    print('Sending\n')
                    connection.send(bytes(f'{addr[0]}:{addr[1]} :', encoding='utf-8') + bytes(data))


    def run(self):
        while True:
            print('Server is running')
            conn, addr = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(conn, addr))
            cThread.demon = True
            cThread.start()
            self.connections.append(conn)
            print(f"Client: {addr[0]}:{addr[1]} connected")


server = Server()
server.run()
