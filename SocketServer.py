import socket, sys
Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerAddress = ('127.1.1.1', 1000)
Sock.bind(ServerAddress)
Sock.listen(1)
while True:
    connection, client_address = Sock.accept()
    try:
        while True:
            DataFromClient = connection.recv(512)
            if DataFromClient:
                connection.sendall(DataFromClient)
            else:
                break       
    finally:
        connection.close()
