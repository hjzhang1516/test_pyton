import unittest
from factorial.src.tp_factorial.factorial import fact, div, plus

class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = fact(5)
        self.assertEqual(res, 120)

    def test_fact_0(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = fact(0)
        self.assertEqual(res, 1)

    def test_div(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = div(5)
        self.assertEqual(res, 2)

    # def test_plus(self):
    #     """
    #     The actual test.
    #     Any method which starts with ``test_`` will considered as a test case.
    #     """
    #     res = plus(5)
    #     self.assertEqual(res, 15)

    def test_error(self):
        """
        To test exception raise due to run time error
        """
        self.assertRaises(ZeroDivisionError, div, 0)


if __name__ == '__main__':
    unittest.main()