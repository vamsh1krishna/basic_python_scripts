#import socket
#finp = input('Enter a url: ')
#ost = finp.split('/')
#words = host[2]
#print(words)

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#try:
#    mysock.connect(('data.pr4e.org', 80))
#    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#    mysock.send(cmd)
#except:
#    print('Enter a valid url')
#    quit()

#while True:
#    if len(data) < 1:
#        break
#    print(data.decode(),end='')

#mysock.close()


import socket

url = 'http://data.pr4e.org/page1.htm'

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
except:
    print('Enter a valid url.')
    quit()
    
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
