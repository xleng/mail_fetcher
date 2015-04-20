#-*- encoding:utf8 -*-
import ConfigParser
import csv
#import multiprocessing
import time
import os
import sqlite3

from writer import Writer
from fetcher import Fetcher

spath = ''

def fetch_count_read(folder):
   f = os.path.join(folder,'cnt.txt')
   cnt = 0
   if os.path.exists(f):
      with open(f, 'rb') as file:
         cnt = int(file.read())

   print cnt
   return cnt




def fetch_task(con_info):

    folder = os.path.join(spath, con_info[0])

    f = Fetcher(con_info[0], con_info[1], con_info[2], int(con_info[3]), con_info[4]=="1", Writer(folder))

    cnt = fetch_count_read(folder)

    total = f.msg_count()

    if total > cnt:
      idList = range(cnt+1,total+1)
      #idList = [40,]
      print idList
      f.fetch(idList)

      #return mail address and fetched number
      return con_info[0], idList[-1]
    else:
      return con_info[0], 0


if __name__ == "__main__":
    #load config file
    config = ConfigParser.RawConfigParser()
    config.read('cfg.ini')

    fpath = config.get('AddressFile', 'location')
    spath = config.get('StorePath', 'path')
    tnumber = int(config.get('Thread', 'number'))
    period = int(config.get('Period', 'time'))
    dbpath = config.get('DBFile', 'location')


    print '-' * 40
    print 'Configuration:'
    print 'account file path:', fpath
    print 'store path:', spath
    print 'thread number:', tnumber
    print 'period:', period ,'minutes'
    print '-' * 40

    t = 0
    while True:
        now = time.time() 

        if now - t > period * 60:
            t = now
            #get account info
            with open(fpath, 'rb') as f:
                #using process pool
                #pool = multiprocessing.Pool(pnumber)

                #using thread pool
                from multiprocessing.dummy import Pool
                pool = Pool(tnumber)
                
                results = pool.map(fetch_task, csv.reader(f))
                print results
                pool.close()
                pool.join()
        else:
            time.sleep(1)
            #print 'sleep'



