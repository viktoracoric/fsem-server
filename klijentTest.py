import socket

serverName = '0.0.0.0'
serverPort = 14010

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((serverName, serverPort))
sock.close()
