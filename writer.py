import time
import os

class Writer(object):
   def __init__(self, folder):
      self.folder = folder
      if not os.path.exists(folder):
         print 'create folder:', folder
         os.makedirs(folder)

   def write(self, eml):
      ftxt = os.path.join(self.folder, eml.Date() + '-' + eml.Subject() + '.txt')

      print 'save file: ', ftxt
      print 'from: ', eml.From()
      print 'to: ', eml.To()
      #print 'date: ', eml.Date()
      #print 'body: ', eml.Content()
      #with open(ftxt, 'wb') as f:
      #   f.write('From: ' + eml.From() + '\r\n')
      #   f.write('To: ' + eml.To() + '\r\n')
      #   f.write(eml.Content())




if __name__ == "__main__":
   from eml import Eml

   w = Writer("/tmp/testf")
   e = Eml(open('test.eml'))

   w.write(e)

