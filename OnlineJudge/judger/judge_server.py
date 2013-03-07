import socket,traceback,time,struct
from setting import *

host = judge_server
port = judge_post
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))

while 1:
    print 'Waiting...'
    message,address=s.recvfrom(1024)
    reply = 'Accept'
    s.sendto(reply,address)
    print 'judge one problem'