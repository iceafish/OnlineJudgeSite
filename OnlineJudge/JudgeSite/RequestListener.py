import sys,os,platform
from datetime import datetime
from django.core.management import setup_environ
from OnlineJudge import settings
import filecmp
import traceback,time,threading
from judger.setting import *
from JRequest.models import RequestList
from problems.models import DataFile,Problem
CUR_DIR = os.getcwd()
sys.path.append(CUR_DIR)
os.environ['DJANGO_SETTINGS_MODULE']='OnlineJudge.settings'
os_name = platform.system()

JudgeQue = Queue(100)


