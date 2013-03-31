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
from problems.models import DataFile,Problem

host = JUDGE_HOST
port = JUDGE_POST
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind((host,port))
os_name = platform.system()

def Compiler( type ):
    #('1', 'GNU C',),('2', 'GNU C++ 4.7',), ('3', 'Microsoft Visual C++ 2010',),('4', 'Java',)
    if type == 1 :
        ce_res = os.system("gcc -fno-asm -O2 -o ./judger/tmp/test.exe %s" % filePath)
    elif type == 2:
        ce_res = os.system("g++ -fno-asm -O2 -o ./judger/tmp/test.exe %s" % filePath)
    #elif type == 3:
    #elif type == 4:
    else:
        print "please write a compile type error log."
        return -1
    return ce_res

def RunTestdata( type, inputfilePath ):
    if type==1 or type==2:
        cmd = "./judger/tmp/test.exe < %s > ./judger/tmp/res.out" % inputfilePath
    else:
        print "please write a compile type error log."
        return
    
    if os_name == 'Linux':
        os.system(cmd)
    elif os_name == 'Windows':
        os.system(cmd.replace('/', '\\'))

def CleanTmp():
    Dir = "./judger/tmp"
    for files in os.listdir(Dir):
        tfile = os.path.join(Dir, files)
        if os.path.isfile(tfile):
            os.remove(tfile.replace('\\\\','/'))
        else:
            print "delete file error."

while True:
    message, addr = s.recvfrom(2048)
    item = RequestList.objects.order_by("-id")[0]
    print addr
    filePath = item.codeFile
    ##############################
    
    
    ques = Problem.objects.get(id = item.problemID)
    print ques

    print ques.TestFile.all()
    
    
    
    
    
    
    
    ##############################
    test_data = DataFile.objects.get( name = item.problemID )
    input_file_address =  './'+str(test_data.in_file)
    output_file_address = './'+str(test_data.out_file)
    
    ce_res = Compiler(item.languageTypeID)
    if ce_res:
        sys_result = 8
    else:
        RunTestdata( item.languageTypeID, input_file_address )
        is_same = filecmp.cmp( "./judger/tmp/res.out", output_file_address )
        if is_same:
            sys_result = 1
        else:
            sys_result = 2

    CleanTmp()
    reply = pack('ii', sys_result, 1)
    s.sendto(reply, addr)