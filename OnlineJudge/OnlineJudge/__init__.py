import threading
import time
from judger.JudgeQue import put,pull,getSize,getReq,isEmpty
from judger.views import submit_code
class MyThread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            print "run threading~"
            if not isEmpty():
                submit_code(None,problem_id = 0)
            time.sleep(5)
mythread = None

def get_and_run():
    global mythread
    if mythread == None:
        mythread = MyThread()
        mythread.start()
get_and_run()

    