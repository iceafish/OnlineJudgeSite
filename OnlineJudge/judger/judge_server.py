import traceback,time
from struct import pack
from setting import *
from socket import *
#from requestQue.models import RequestList


host = judge_server
port = judge_post
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind((host,port))

while 1:
    print 'Waiting...'
    message, addr = s.recvfrom(2048)
    #run  judge
    sys_result = 1
    reply = pack('ii', sys_result, 1)
    s.sendto(reply, addr)
    print 'judge one problem'