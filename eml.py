import email
import time

class Eml(object):
   def __init__(self, file):
      self.msg = email.message_from_file(file)

   def Subject(self):
      subject = self.msg.get('Subject')
      head = email.Header.Header(subject)
      dec_head = email.Header.decode_header(head)
      #print dec_head
      #print 'subject: ', dec_head[0][0]
      return (dec_head[0][0] or '').translate(None, '\t\r\n')

   def Date(self):
      return  self.msg.get("date")

   def From(self):
      #print 'from: ', email.utils.parseaddr(self.msg.get("from"))[1] 
      return email.utils.parseaddr(self.msg.get("from"))[1] 

   def To(self):
      #print 'to: ', email.utils.parseaddr(self.msg.get("to"))[1] 
      return email.utils.parseaddr(self.msg.get("to"))[1] 

   def Content(self):
      conts = ''
      #headers = msg.items()[0]
      for part in self.msg.walk():
         # multipart/* are just containers
         if part.get_content_maintype() == 'multipart':
            continue
         conttype = part.get_content_type()
         print conttype

         #if conttype.startswith('text'):
         if conttype == "text/plain":
            #print base64.decodestring(part.get_payload())
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



