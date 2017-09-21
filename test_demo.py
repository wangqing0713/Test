import unittest
from count import Count


class TestDemo(unittest.TestCase):

    def setUp(self):
        pass

    def test_case1(self):
        self.a = Count(2, 3).add()
        self.assertEqual(self.a, 5)
        print "ok"

    def test_case2(self):
        self.a = Count("AAA", "BBB").add()
        self.assertEqual(self.a, "AAABBB")
        print "ok2"

    def test_case3(self):
        self.a = Count(2.33, 2.66).add()
        self.assertEqual(self.a, 4.99)
        print "ok3"

    def tearDown(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestDemo("test_case2"))
    suite.addTest(TestDemo("test_case3"))
    runner = unittest.TextTestRunner()
    runner.run(suite)