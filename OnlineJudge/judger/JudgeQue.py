from Queue import Queue
from setting import JUDGEQUE_SIZE

req = Queue(maxsize = JUDGEQUE_SIZE)

def put( item ):
    req.put( item )
    
def pull():
    return req.get()

def getSize():
    return req.qsize()
def getReqID():
    return id(req)

