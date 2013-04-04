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

host = ''
port = JUDGE_POST
s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind((host,port))
s.listen(4)
os_name = platform.system()

def Compiler( type, filePath ):
    #('1', 'GNU C',),('2', 'GNU C++ 4.7',), ('3', 'Microsoft Visual C++ 2010',),('4', 'Java',)    
    if type == 1 :
        if os_name == 'Linux':
            ce_res = os.system("gcc %s -o ./judger/tmp/test.exe -ansi -fno-asm -O2 -Wall -lm --static -DONLINE_JUDGE" % filePath)
        elif os_name == 'Windows':
            ce_res = os.system("gcc -static -fno-optimize-sibling-calls -fno-strict-aliasing -DONLINE_JUDGE -fno-asm -lm -s -Wl,--stack=268435456 -O2 -o ./judger/tmp/test.exe %s" % filePath)
        else:
            print os_name
            return -1
    elif type == 2:
        if os_name == 'Linux':
            ce_res = os.system("g++ %s -o ./judger/tmp/test.exe -ansi -fno-asm -O2 -Wall -lm --static -DONLINE_JUDGE" % filePath)
        elif os_name == 'Windows':
            ce_res = os.system("g++ -static -fno-optimize-sibling-calls -fno-strict-aliasing -DONLINE_JUDGE -lm -s -x c++ -Wl,--stack=268435456 -O2 -o ./judger/tmp/test.exe %s" % filePath)
        else:
            print os_name
            return -1
    #elif type == 3:
    elif type == 4:
        ce_res = os.system("g++ %s -o ./judger/tmp/test.exe -ansi -fno-asm -O2 -Wall -lm --static -DONLINE_JUDGE" % filePath)
    else:
        print "please write a compile type error log."
        return -1
    return ce_res

def RunTestdata( type, inputfilePath, outfilePath ):
    if type==1 or type==2:
        cmd = "./judger/tmp/test.exe < %s > ./judger/tmp/%s.out" % ( inputfilePath, outfilePath )
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
        print files
        tfile = os.path.join(Dir, files)
        if os.path.isfile(tfile):
            os.remove(tfile.replace('\\\\','/'))
        else:
            print "delete file error."

def RunServer():
    print "Server is running on port %d" % port
    while True:
        clientsock, clientaddr = s.accept()
        msg = clientsock.recv(1024)
        if msg:
            item = RequestList.objects.get(id = msg)
        filePath = item.codeFile
        ques = Problem.objects.get(id = item.problemID)
        ce_res = Compiler( item.languageTypeID, filePath )
        
        if ce_res:
            sys_result = 8
        else:
            DataNumb = 0
            for test_data in ques.TestFile.all():
                DataNumb += 1
                InputData =  './'+str(test_data.in_file)
                OutputData = 'test' + str(DataNumb)
                SampleOutputData = './'+str(test_data.out_file)
                RunTestdata( item.languageTypeID, InputData, OutputData )
                is_same = filecmp.cmp( "./judger/tmp/%s.out"%OutputData, SampleOutputData )
                if not is_same:
                    break
                
            if is_same:
                sys_result = 1
            else:
                sys_result = 2
        
        CleanTmp()
        reply = pack('ii', sys_result, 1)
        clientsock.sendall(reply)
        clientsock.close()
    s.close()

RunServer()