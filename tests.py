import unittest

from src_50th_week import boj1236


class testsuite(unittest.TestCase):
    def testcase_001(self):
        res = boj1236.solve(self, 4, 4, ["....", "....", "....", "...."])
        self.assertEqual(4, res)


if __name__ == "__main__":
    unittest.main()

'''
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
'''

'''
from src_49th_week import boj2851


class testsuite(unittest.TestCase):
    def testcase_001(self):
        res = boj2851.solve([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        self.assertEqual(100, res)

    def testcase_002(self):
        res = boj2851.solve([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(100, res)


if __name__ == "__main__":
    unittest.main()
'''
