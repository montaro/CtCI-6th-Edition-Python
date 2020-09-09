import unittest


def is_substring(string, sub):
    return string.find(sub) != -1


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)
    return False


class MyTestCase(unittest.TestCase):
    def test_string_rotation(self):
        self.assertTrue(string_rotation('waterbottle', 'erbottlewat'))
        self.assertFalse(string_rotation('foo', 'bar'))
        self.assertFalse(string_rotation('foo', 'foofoo'))


if __name__ == '__main__':
    unittest.main()
