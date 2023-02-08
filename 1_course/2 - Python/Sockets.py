#!/bin/python3

import socket

HOST = "127.0.0.1"
PORT = 7777

# AF_INET -> IPv4(connecting via IPv4), SOCK_STREAM -> port #
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
