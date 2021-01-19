import socket

serverName = '0.0.0.0'
serverPort = 14010

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((serverName, serverPort))
zahtjev = "PUBLISH\r\nEMAIL: email_adresa\r\nECDH KEY PART: javni dio_DH\r\n"
sock.send(zahtjev.encode())
sock.close()
