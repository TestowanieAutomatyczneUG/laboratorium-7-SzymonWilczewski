import unittest

from src.zad02.main import Password
from parameterized import parameterized, parameterized_class


class PasswordParameterizedPackage(unittest.TestCase):

    @parameterized.expand([
        ("ABCDEF123456!?", True),
        ("123!!!123ABC", True),
        ("Password$123", True),
        ("abcdef123456!?", False),
        ("123123ABC", False),
        ("PASSWORD!!!", False),
        ("!!!!!!!!", False),
        ("A1!", False),
    ])
    def test_valid_password(self, password, expected):
        self.assertEqual(self.tmp.ValidPassword(password), expected)

    def setUp(self):
        self.tmp = Password()

    @parameterized.expand([
        (True, TypeError),
        ("Pass word 123 !!!", ValueError),
    ])
    def test_valid_password_exceptions(self, password, expected):
        with self.assertRaises(expected):
            self.tmp.ValidPassword(password)


@parameterized_class(('password', 'expected'), [
    ("ABCDEF123456!?", True),
    ("123!!!123ABC", True),
    ("Password$123", True),
    ("abcdef123456!?", False),
    ("123123ABC", False),
    ("PASSWORD!!!", False),
    ("!!!!!!!!", False),
    ("A1!", False),
])
class PasswordParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = Password()

    def test_valid_password_2(self):
        self.assertEqual(self.tmp.ValidPassword(self.password), self.expected)


if __name__ == '__main__':
    unittest.main()
