import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org', 80)) #connect to port 80 on remote server

cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() # to UTF8
mySock.send(cmd)

while True:
    data = mySock.recv(512) #get 512 characters
    if len(data) < 1:
        break
    print(data.decode(), end='') #to Unicode

mySock.close()
