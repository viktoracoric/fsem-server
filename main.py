import socket
import sys
from subprocess import call

serverName = '0.0.0.0'
serverPort = 14010

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAdresa = (serverName, serverPort)
sock.bind(serverAdresa)

sock.listen(1)
print("Server je spreman")

while True:
    veza, klijentAdresa = sock.accept()
    zahtjev = veza.recv(1024)
    zahtjev = zahtjev.decode()
    print(zahtjev)
    zahtjev.split("\r\n")
    print(zahtjev)
    if zahtjev[0] == 'PUBLISH':
	    print("Lol")
    call(["python", "DiffieHellman.py"])
    veza.close()
