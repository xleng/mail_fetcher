#-*- encoding:utf8 -*-
import email
import time
import chardet

class Eml(object):
   def __init__(self, file):
      self.msg = email.message_from_file(file)
      #print self.msg

   def Subject(self):
      subject = self.msg.get('Subject')
      if subject is None:
         print 'subject is None, return'
         return ''
      #print subject
      head = email.Header.Header(subject, charset=chardet.detect(subject).get('encoding'))
      #print head
      dec_head = email.Header.decode_header(head)
      #print dec_head
      if len(dec_head) == 0:
         return ''

      s = ''
      if dec_head[0][1] is None:
         s = dec_head[0][0] or ''
      else:
         if dec_head[0][0] is None:
            s = ''
         else:
            s = dec_head[0][0].decode(dec_head[0][1], 'ignore')
            
      return s

   def Date(self):
      t = email.utils.parsedate(self.msg.get("date"))
      if t is None:
         t = time.localtime()
      return time.strftime('%Y%m%d-%H%M%S', t)

   def From(self):
      #print 'from: ', email.utils.parseaddr(self.msg.get("from"))[1] 
      return email.utils.parseaddr(self.msg.get("from"))[1] 

   def To(self):
      #print 'to: ', email.utils.parseaddr(self.msg.get("to"))[1] 
      return email.utils.parseaddr(self.msg.get("to"))[1] 

   def Content(self):
      conts = ''
      for part in self.msg.walk():
         # multipart/* are just containers
         if part.get_content_maintype() == 'multipart':
            continue
         conttype = part.get_content_type()
         print conttype

         if conttype.startswith('text'):
         #if conttype == "text/plain":
            #print base64.decodestring(part.get_payload())
            print part.get_payload()
            conts += part.get_payload(decode=True)

      return conts
         



if __name__ == "__main__":
    fname = "test.eml"
    print '-' * 20, fname, '-' * 20
    eml = Eml(open(fname))
    print "Subject:",eml.Subject()
    print "Date:", eml.Date()
    print "From:",eml.From()
    print "To:",eml.To()
    print "Contents: "
    print eml.Content()



