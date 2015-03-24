#-*- encoding:utf8 -*-

import cStringIO
import poplib
import email
import base64

class MailFetcher:
   def __init__(self, user, passwd, pserver, pport):
      self.user = user
      self.passwd = passwd
      self.pserver = pserver
      self.pport = pport

   def Fetch(self):
      print self.user, self.pserver, self.pport
      mclient = poplib.POP3_SSL(self.pserver, self.pport)
      mclient.set_debuglevel(1)
      mclient.user(self.user)
      mclient.pass_(self.passwd)

      #print mclient.stat()
      msgnum = len(mclient.list()[1])
      print 'message number: %d ' % msgnum

      for i in range(msgnum):
      #for i in range(1):
         buf = cStringIO.StringIO()
         for j in mclient.retr(i+1)[1]:
            #print j
            print >> buf, j
         buf.seek(0)

         msg = email.message_from_file(buf)

         #headers = msg.items()[0]
         subject = msg.get('Subject')
         head = email.Header.Header(subject)
         dec_head = email.Header.decode_header(head)
         #print dec_head
         print 'subject: ', dec_head[0][0]
         print 'from: ', email.utils.parseaddr(msg.get("from"))[1] 
         print 'to: ', email.utils.parseaddr(msg.get("to"))[1] 
         for part in msg.walk():
            # multipart/* are just containers
            if part.get_content_maintype() == 'multipart':
               continue
            conttype = part.get_content_type()
            print conttype
            #if conttype.startswith('text'):
            #   print base64.decodestring(part.get_payload())

      mclient.quit()



if __name__ == "__main__":
   mr = MailFetcher()

   mr.Fetch()
