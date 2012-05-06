'''
Created on May 6, 2012

@author: bryan.hunt
'''
import unittest
from rp1210 import j1939Message
import copy

class j1939MessageTestCase(unittest.TestCase):
    def setUp(self):
        self.Message = j1939Message(0, 126720, 6, 1, 3, "\x00\x01\x02\x03\x04\x05\x06\x07")
        
class j1939MessageToStringTestCase(j1939MessageTestCase):
    def runTest(self):
        assert str(self.Message) == "\x00\xEF\x01\x06\x01\x03\x00\x01\x02\x03\x04\x05\x06\x07"
        
class j1939MessageFromStringTestCase(j1939MessageTestCase):
    def runTest(self):
        newMessage = copy.copy(self.Message)
        newMessage.fromString("\x01\x00\x00\x00\x00\xEF\x01\x06\x01\x03\x00\x01\x02\x03\x04\x05\x06\x07")
        assert str(self.Message) == str(newMessage)