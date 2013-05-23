import sys,os,platform
from datetime import *
import filecmp
CUR_DIR = os.getcwd()
sys.path.append(CUR_DIR)
os.environ['DJANGO_SETTINGS_MODULE']='OnlineJudge.settings'
from django.core.management import setup_environ
from OnlineJudge import settings

import traceback,time,threading
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
is_ready = False
time_out = False
StartTime = 0
EndTime = 0

class runThread(threading.Thread):
    
    def __init__(self, langTypeID, problem):
        threading.Thread.__init__(self)
        self.langTypeID = langTypeID
        self.id = problem
    def run(self):
        global is_ready,StartTime,EndTime
        StartTime = time.clock()
        DataNumb = 0
        ques = Problem.objects.get(id = self.id)
        for test_data in ques.TestFile.all():
            DataNumb += 1
            InputData =  './'+str(test_data.in_file)
            OutputData = 'test' + str(DataNumb)
            RunTestdata( self.langTypeID, InputData, OutputData )
        is_ready = True
        EndTime = time.clock()
        
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
    elif type == 4:
        ce_res = os.system("g++ %s -o ./judger/tmp/test.exe -ansi -fno-asm -O2 -Wall -lm --static -DONLINE_JUDGE" % filePath)
    else:
        print "please write a compile type error log."
        return -1
    return ce_res

def JudgeInit():
    
    global is_ready,StartTime,EndTime,time_out
    is_ready = False
    time_out = False
    StartTime = 0
    EndTime = 0

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
            os.remove(tfile.replace('\\','/'))
        else:
            print "delete file error."

def killer():
    global time_out,is_ready
    if not is_ready :
        time_out = True
    return

def RunServer():
    
    print "Server is running on port %d" % port
    while True:
        print '=================='
        clientsock, clientaddr = s.accept()
        print clientaddr
        msg = clientsock.recv(1024)
        if msg:
            item = RequestList.objects.get(id = msg)
        else:
            return 
        filePath = item.codeFile
        ques = Problem.objects.get(id = item.problemID)
        ce_res = Compiler( item.languageTypeID, filePath )
        JudgeInit()
        if ce_res:
            sys_result = 8
        else:
            global StartTime,EndTime,is_ready
            kTimer = threading.Timer( ques.TimeLimit+ques.TimeLimit*0.1 , killer )
            Judger = runThread(item.languageTypeID, item.problemID)
            Judger.setDaemon(True)
            kTimer.start()
            Judger.start()
            print "thread good."            

#kTimer.join()
            ####### this part is killer body #######
            while ( not is_ready and not time_out ):
                time.sleep(0.1)
                
            DataNumb = 0
            for test_data in ques.TestFile.all():
                DataNumb += 1
                OutputData = 'test' + str(DataNumb)
                SampleOutputData = './' + str(test_data.out_file)
                is_same = filecmp.cmp( "./judger/tmp/%s.out" % OutputData, SampleOutputData )
                if not is_same:
                    break
            if is_same:
                sys_result = 1
            else:
                sys_result = 2
                    
            if ( not is_ready ):
                if os_name == 'Windows':
                    os.system('taskkill /f /im test.exe')
                elif os_name == 'Linux':
                    os.system('killall test.exe')
                sys_result = 4
                EndTime = time.clock()
        
        timeused = (int)(EndTime-StartTime)*1000
        reply = pack('ii', sys_result, timeused)
        clientsock.send(reply)
        #################################
        clientsock.close()
        CleanTmp()
    s.close()
    
if __name__=='__main__':
    
    RunServer()
