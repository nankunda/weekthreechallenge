import unittest
from missing_list import missing_number_list


class test_missing(unittest.TestCase):

    def test_missingNumber(self):
        self.assertListEqual(missing_number_list(
            [1, 2, 3, 5, 6, 7, 9]), [4, 8])
        self.assertEqual(len(missing_number_list([1, 2, 3, 5, 6, 7, 9])), 2)

    def test_input_is_list(self):
        self.assertEqual(missing_number_list(
            (1, 3, 4)), 'only lists are allowed')


if __name__ == '__main__':
    unittest.main()