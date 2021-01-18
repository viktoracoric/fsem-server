import socket
import sys

serverName = '0.0.0.0'
serverPort = 14010

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAdresa = (serverName, serverPort)
sock.bind(serverAdresa)

sock.listen(1)
print("Server je spreman")

while True:
    veza, klijentAdresa = sock.accept()
    # kod ide ovdje
    veza.close()
