import sys,os
from datetime import *
CUR_DIR = os.getcwd()
sys.path.append(CUR_DIR)
os.environ['DJANGO_SETTINGS_MODULE']='OnlineJudge.settings'
from django.core.management import setup_environ
from OnlineJudge import settings

import traceback,time
from struct import pack
from judger.setting import *
from socket import *

from judger.models import RequestList
from judger.JudgeQue import put,pull,getSize

host = JUDGE_HOST
port = JUDGE_POST
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind((host,port))

while 1:
    print 'Waiting...'
    print getSize()
    message, addr = s.recvfrom(2048)
    
    #run  judge
    sys_result = 1
    reply = pack('ii', sys_result, 1)
    s.sendto(reply, addr)
    print 'judge one problem'