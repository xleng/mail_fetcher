#-*- encoding:utf8 -*-
import time
import os
import re

class Writer(object):
   def __init__(self, folder):
      self.folder = folder
      self.fcnt = os.path.join(self.folder, 'cnt.txt')
      if not os.path.exists(folder):
         print 'create folder:', folder
         os.makedirs(folder)

   def write(self, eml, cnt):
      #replay space, / ! &to - in file name
      s = re.sub(r'[\s/!&]', '-', eml.Subject())
      ftxt = os.path.join(self.folder, eml.Date() + '-' + s + '.txt')

      print 'save file: ', ftxt
      print 'subject: ', eml.Subject()
      print 'from: ', eml.From()
      print 'to: ', eml.To()
      print 'date: ', eml.Date()
      #print 'body: ', eml.Content()
      with open(ftxt, 'wb') as f:
         #f.write('Subject: ' + eml.Subject().encode('utf-8', 'ignore') + '\r\n')
         f.write('From: ' + eml.From() + '\r\n')
         f.write('To: ' + eml.To() + '\r\n')
         f.write(eml.Content())

      #write the index
      with open(self.fcnt, 'w') as file:
         file.write(str(cnt))


if __name__ == "__main__":
   from eml import Eml

   w = Writer("/tmp/testf")
   e = Eml(open('test.eml'))

   w.write(e)

