import ConfigParser
import csv
#import multiprocessing
import time
import os

spath = ''

def fetch_task(con_info):

    folder = os.path.join(spath, con_info[0])
    if not os.path.exists(folder):
        print 'create folder:', folder
        os.makedirs(folder)

    #return mail address and fetched number
    return con_info[0], 2

if __name__ == "__main__":
    #load config file
    config = ConfigParser.RawConfigParser()
    config.read('cfg.ini')

    fpath = config.get('AddressFile', 'location')
    spath = config.get('StorePath', 'path')
    tnumber = int(config.get('Thread', 'number'))
    period = int(config.get('Period', 'time'))

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



