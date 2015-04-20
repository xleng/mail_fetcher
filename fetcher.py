#-*- encoding:utf8 -*-

import cStringIO
import poplib
import re
#import base64
from eml import Eml

class Fetcher:
   def __init__(self, user, passwd, pserver, pport, bssl, writer=None):
      self.pserver = pserver
      self.pport = pport
      self.writer = writer
      if bssl:
         self.mclient = poplib.POP3_SSL(self.pserver, self.pport)
      else:
         self.mclient = poplib.POP3(self.pserver, self.pport)

      self.mclient.set_debuglevel(1)
      self.mclient.user(user)
      self.mclient.pass_(passwd)
   
   def __del__(self):
      if self.mclient:
         self.mclient.quit()

   def msg_count(self):
      msgnum = self.mclient.stat()[0]
      print 'message number: %d ' % msgnum
      return msgnum


   def fetch(self, idList):
      for i in idList:
         buf = cStringIO.StringIO()
         #print self.mclient.retr(i)[1]
         for line in self.mclient.retr(i)[1]:
            line = re.sub(r'\r', '', line)
            print >> buf, line
         buf.seek(0)

         self.writer.write(Eml(buf), i)




#if __name__ == "__main__":

