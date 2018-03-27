import socket
import threading
import sys

class Server:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connections= []

        def __init__(self):
                self.sock.bind(('0.0.0.0',5000))
                self.sock.listen(1)
        def handler(self,c,a):
            global connections
            while True:
                data=c.recv(1024)
                for connection in self.connections:
                    connection.send(bytes(data))
                if not data:
                   print(str(a[0]) + ':' + str(a[1]),'Disconnected') 
                   self.connections.remove(c) 
                   c.close()
                   break
        def run(self):
            while True:
                c,a =self.sock.accept()
                cThread = threading.Thread(target=self.handler,args=(c,a))
                cThread.daemon=True
                cThread.start()
                self.connections.append(c)
                print(str(a[0]) + ':' + str(a[1]),"connected")

class Client:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def send_msg(self):
        self.sock.send(bytes(input('','utf-8')))
    def __init__(self,address):
        self.sock.connect((address,1000))
        ithread= threading.Thread(target=self.send_msg)
        ithread.start()
        while True:
            data =self.sock.recv(1024)
            if not data:
                break
            print(data)


if(len(sys.argv)>1):
    client = Client(sys.argv[1])
else:
    server = Server()
    server.run()