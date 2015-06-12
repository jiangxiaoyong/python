'''
Created on May 30, 2015

@author: jxy
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.2",1025))
s.listen(1025)
print ("Listening on port 443...")
(client, (ip, port)) = s.accept()
print "receive connection from : {ip_1}".format(ip_1 = ip)

while True:
    command = raw_input("~# ")
    code = bytearray(command)
    
    client.send(code)
    data = client.recv(1024)
    decode = bytearray(data)
    print decode
    
client.close()
s.close()