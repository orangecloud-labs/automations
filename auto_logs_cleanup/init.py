# SCRIPT NAME /log-removal.py
import sys
import os
import glob

# MIN AND MAX DEFINED IN BYTES
MAX = XXXXXXXXXX
MIN = YYYYYYYYYY

# DEFINE PATH TO RAW LOGS
PATH = "/var/log/nginx/"
def map(list):
        if list == "":
                list = glob.glob(PATH +"*.log")
                print list
        for line in  sorted(list):
                print line
                remove(line, list)
def remove(file, list):
        os.system("rm "+ file)
        list.remove(file)
        print list
        recheck(list)
def recheck(list):
        size = 0
        for (path_, dir_, files_) in os.walk(PATH):
                for file_ in files_:
                        fname_ = os.path.join(path_, file_)
                        size += os.path.getsize(fname_)
        print size
        dsize()
        if size > MIN:
                sys.exit()
                map(list)
        if size < MIN:
                sys.exit()
def dsize():
        size = 0
        for (path_, dir_, files_) in os.walk(PATH):
                for file_ in files_:
                        fname_ = os.path.join(path_, file_)
                        size += os.path.getsize(fname_)
        print size
        if size > MAX:
                map("")
dsize()
