import sys,os,platform
from datetime import *
import filecmp
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
from problems.models import DataFile
from judger.JudgeQue import put,pull,getSize

##
'''test'''
from judger.JudgeQue import getReqID
##

host = JUDGE_HOST
port = JUDGE_POST
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind((host,port))

while 1:
    print 'Waiting...'
    message, addr = s.recvfrom(2048)
    #run  judge
    item = RequestList.objects.order_by("-id")[0]
    filePath = item.codeFile
    os_name = platform.system()
    if os_name == "Linux":
        ce_res = os.system("g++ -fno-asm  -O2  -o ./judger/tmp/test.out %s" % filePath)
        if ce_res != 0 :
            sys_result = 8
        else:
            test_data = DataFile.objects.get( name = item.problemID )
            input_file_address =  './'+str(test_data.in_file)
            output_file_address = './'+str(test_data.out_file)
           	#print input_file_address 
            os.system("./judger/tmp/test.out <%s >./judger/tmp/res.out" % input_file_address)
            is_same = filecmp.cmp("./judger/tmp/res.out",output_file_address)
            if is_same:
                sys_result = 1
            else:
                sys_result = 2
    elif os_name == "Windows":
        sys_result = 1

    reply = pack('ii', sys_result, 1)
    s.sendto(reply, addr)
    print 'judge one problem'
