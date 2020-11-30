import unittest
from src_49th_week import boj15953

class testsuite(unittest.TestCase):
    def testcase_001(self):
        s = boj15953.solve(self, 8, 4)
        self.assertEqual(1780000, s)
    def testcase_002(self):
        s = boj15953.solve(self, 13, 19)
        self.assertEqual(620000, s)
    def testcase_003(self):
        s = boj15953.solve(self, 8, 10)
        self.assertEqual(1140000, s)
    def testcase_004(self):
        s = boj15953.solve(self, 18, 18)
        self.assertEqual(420000, s)
    def testcase_005(self):
        s = boj15953.solve(self, 8, 25)
        self.assertEqual(820000, s)
    def testcase_006(self):
        s = boj15953.solve(self, 13, 16)
        self.assertEqual(620000, s)
    def testcase_007(self):
        s = boj15953.solve(self, 22, 32)
        self.assertEqual(0, s)


if __name__ == "__main__":
    unittest.main()
