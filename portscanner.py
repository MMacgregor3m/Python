#port scanner
import socket

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= "137.74.187.100"
port= 443

def postScanner (porty):
    if s.connect_ex