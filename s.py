#!/bin/python3
#sockets
import socket
HOST='127.0.0.1'
PORT= 7777
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AFINET is ipv4 sock_stream is a port

s.connect((HOST,PORT))
