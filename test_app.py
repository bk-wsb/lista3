import unittest
from app import calculate_delta


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate_delta(1, 2, -3), 16)
        self.assertEqual(calculate_delta(2, 7, 6), 1)
        self.assertEqual(calculate_delta(1, -4, 3), 4)
        self.assertEqual(calculate_delta(1, -5, 6), 1)
        self.assertEqual(calculate_delta(1, 0, 9), -36)


if __name__ == "__main__":
    unittest.main()
