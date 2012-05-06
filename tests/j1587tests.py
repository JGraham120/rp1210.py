'''
Created on May 6, 2012

@author: bryan.hunt
'''
import unittest
from rp1210 import j1587Message
import copy

class j1587MessageTestCase(unittest.TestCase):
    def setUp(self):
        self.Message = j1587Message(0, 6, 128, "\x00\x01\x02\x03\x04\x05\x06\x07")
        
class j1587MessageToStringTestCase(j1587MessageTestCase):
    def runTest(self):
        assert str(self.Message) == "\x06\x80\x00\x01\x02\x03\x04\x05\x06\x07"
        
class j1587MessageFromStringTestCase(j1587MessageTestCase):
    def runTest(self):
        newMessage = copy.copy(self.Message)
        newMessage.fromString("\x01\x00\x00\x00\x80\x00\x01\x02\x03\x04\x05\x06\x07")
        assert str(self.Message) == str(newMessage)