#-*- encoding:utf8 -*-

import cStringIO
import poplib
#import base64
from eml import Eml

class Fetcher:
   def __init__(self, pserver, pport, bssl, writer=None):
      self.pserver = pserver
      self.pport = pport
      self.bssl = bssl
      self.writer = writer
      self.mclient = None

   def fetch(self, user, passwd):
      print self.pserver, self.pport, self.bssl
      if self.bssl:
         mclient = poplib.POP3_SSL(self.pserver, self.pport)
      else:
         mclient = poplib.POP3(self.pserver, self.pport)

      mclient.set_debuglevel(1)
      mclient.user(user)
      mclient.pass_(passwd)

      #print mclient.stat()
      msgnum = len(mclient.list()[1])
      print 'message number: %d ' % msgnum

      for i in range(msgnum):
      #for i in range(9):
        buf = cStringIO.StringIO()
        for j in mclient.retr(i+1)[1]:
           #print j
           print >> buf, j
        buf.seek(0)
        self.writer.write(Eml(buf))

      mclient.quit()



#if __name__ == "__main__":
