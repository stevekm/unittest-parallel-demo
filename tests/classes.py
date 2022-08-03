import unittest
from datetime import datetime

class CustomTestCase(unittest.TestCase):
    def setUp(self):
        self.test_label = "{}.{}".format(type(self).__name__, self._testMethodName)
        print("\n>>> starting test: {}".format(self.test_label))
        self.start_time = datetime.now()

    def tearDown(self):
        self.stop_time = datetime.now()
        self.time_elapsed = self.stop_time - self.start_time
        print("\n>>> stopping test: {} ({})".format(self.test_label, self.time_elapsed))
