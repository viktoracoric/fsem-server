import socket
import sys
from subprocess import call
from subprocess import run

serverName = '0.0.0.0'
serverPort = 14010

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAdresa = (serverName, serverPort)
sock.bind(serverAdresa)

sock.listen(1)
print("Server je spreman")

while True:
    veza, klijentAdresa = sock.accept()
    call(["python", "datoteka.py", "smece"])
    call(["python", "enkripcija.py", "d"])
    zahtjev = veza.recv(1024)
    zahtjev = zahtjev.decode()
    zahtjev = zahtjev.splitlines()
    zahtjev[1] = zahtjev[1].rstrip()
    x = zahtjev[1].find(":") + 2
    if zahtjev[0] == 'PUBLISH':
        zahtjev[2] = zahtjev[2].rstrip()
        y = zahtjev[2].find(":") + 2
        call(["python", "datoteka.py", zahtjev[0], zahtjev[1][x:], zahtjev[2][y:]])
    if zahtjev[0] == 'GET':
        kljuc = run(["python", "datoteka.py", zahtjev[0], zahtjev[1][x:]], capture_output=True).stdout
        kljuc = kljuc.decode()
        kljuc = kljuc.rstrip()
        kljuc = kljuc.encode()
        veza.send(kljuc)
    call(["python", "enkripcija.py", "e"])
    veza.close()
