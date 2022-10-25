import comparison
import unittest

class TestComparison(unittest.TestCase):
      def test_compare_string(self):
           self.assertEqual(comparison.comparisonOfTwoStrings("two","two"),True)

      def test_compare_digits(self):
           self.assertEqual(comparison.comparisonOfTwoDigits(2,2),"The Numbers are not equal")

if __name__ == '__main__':
    unittest.main()