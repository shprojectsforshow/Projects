import socket

serversocket = socket.socket(socket.AF_INET, socket.SCOK_STREAM)

host = socket.gethostname()

port = 9999

serversocket.bind((host, port))

serversocket.listen(1)

while True:
    clientsocket, addr = serversocket.accept()

    message = 'Welcome to the server'
    clientsocket.send(message.encode())

    clientsocket.clost()