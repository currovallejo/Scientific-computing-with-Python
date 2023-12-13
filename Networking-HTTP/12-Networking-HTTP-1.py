# PYTHON WEB BROWSER

import socket

# # make a phone call

# # make the socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# # make the connection to port 80
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()
