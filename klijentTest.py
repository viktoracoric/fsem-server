import socket

serverName = '0.0.0.0'
serverPort = 14010

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((serverName, serverPort))

# Za drugu vrstu zahtjeva samo komentirati i odkomentirati linije po potrebi

zahtjev = "PUBLISH\r\nEMAIL: ivo.ivic@gmail.com\r\nECDH KEY PART: jifdqewnfqnf23r\r\n"
#zahtjev = "GET\r\nEMAIL: ivo.ivic@gmail.com\r\n"

sock.send(zahtjev.encode())
rezultat = sock.recv(1024)
print(rezultat.decode())
sock.close()
