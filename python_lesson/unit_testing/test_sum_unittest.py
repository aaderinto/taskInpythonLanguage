import bodmas
import unittest

class TestBodmas(unittest.TestCase):
      def test_addition_output(self):
           self.assertEqual(bodmas.add(3, 2),5)

      def test_sub_output(self):
           self.assertEqual(bodmas.subtraction(7, 6),1)

if __name__ == '__main__':
    unittest.main()