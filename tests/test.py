
import unittest
from rp1210 import RP1210

class RP1210TestCase(unittest.TestCase):
    def setUp(self):
        self.rp1210 = RP1210()
        self.ClientId = self.rp1210.ClientConnect(1, 'J1939', 0, 0)

class RP1210ReadVersionTestCase(RP1210TestCase):
    def runTest(self):
        """Test DLL Reports Version"""
        assert self.rp1210.ReadVersion() 

class RP1210ClientConnectTestCase(RP1210TestCase):
    def runTest(self):
        """Test driver successfully connected to the device"""
        assert (self.ClientId < 128), 'Connection Failure: %d' % self.ClientId
    def tearDown(self):
        self.rp1210.ClientDisconnect(self.ClientId)
        
class RP1210ReadDetailedVersionTestCase(RP1210TestCase):
    def runTest(self):
        """Test DLL Report Detailed Version Information"""
        assert self.rp1210.ReadDetailedVersion(self.ClientId)
                 

#testCase1 = RP1210ReadVersionTestCase()
#testCase2 = RP1210ClientConnectTestCase()
#testCase3 = RP1210ReadDetailedVersionTestCase()
