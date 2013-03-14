import sys,os
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
    #print "and Queue's length = "+str(getSize())
    #print "judge_server getReqID = ",getReqID()
    message, addr = s.recvfrom(2048)
    #run  judge
    ''' from queue get a item. '''
    '''print getSize()
    
    item = pull()'''
    #print message , addr
    item = RequestList.objects.order_by("-id")[0]
    filePath = item.codeFile
    #print filePath
    
    ce_res = os.system("g++ -fno-asm  -O2  -o ./judger/tmp/test.out %s" % filePath)
    if ce_res != 0 :
        sys_result = 8
    else:
        input_file_address = "./judger/judge_data/"+str(item.problemID)+"/input.txt"
        output_file_address =  "./judger/judge_data/"+str(item.problemID)+"/output.txt"
        #print "./judger/tmp/test.out <%s >./judger/tmp/res.txt" % input_file_address
        os.system("./judger/tmp/test.out <%s >./judger/tmp/res.txt" % input_file_address)
        is_same = filecmp.cmp("./judger/tmp/res.txt",output_file_address)
        if is_same:
            sys_result = 1
        else:
            sys_result = 2
    #################################################
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    ##################################################
    #sys_result = 1
    reply = pack('ii', sys_result, 1)
    s.sendto(reply, addr)
    print 'judge one problem'