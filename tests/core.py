
import unittest
from rp1210 import RP1210

class InitTestCase(unittest.TestCase):
    def setUp(self):
        self.rp1210 = RP1210()
        self.ClientId = self.rp1210.ClientConnect(1, 'J1939', 0, 0)
    def tearDown(self):
        self.rp1210.ClientDisconnect(self.ClientId)

class ClientConnectTestCase(InitTestCase):
    def runTest(self):
        """Test driver successfully connected to the device"""
        assert (self.ClientId < 128), 'Connection Failure: %d' % self.ClientId
        
class ReadVersionTestCase(InitTestCase):
    def runTest(self):
        """Test DLL Reports Version"""
        assert self.rp1210.ReadVersion() 
      
class ReadDetailedVersionTestCase(InitTestCase):
    def runTest(self):
        """Test DLL Report Detailed Version Information"""
        assert self.rp1210.ReadDetailedVersion(self.ClientId)
                 
