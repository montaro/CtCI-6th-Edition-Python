import unittest
from collections import Counter

A = ord('A')
Z = ord('Z')
a = ord('a')
z = ord('z')


def palindrome_permutation(phrase):
    phrase = phrase.lower()
    no_of_odd = 0
    counter = Counter(phrase)
    for k, v in counter.items():
        if is_char(k):
            if v % 2 == 1:
                no_of_odd = no_of_odd + 1
                if no_of_odd > 1:
                    return False
    return True


def is_char(c):
    o = ord(c)
    if A <= o <= Z or a <= o <= z:
        return True
    return False


class MyTestCase(unittest.TestCase):
    def test_is_char(self):
        self.assertTrue(is_char('a'))
        self.assertTrue(is_char('z'))
        self.assertTrue(is_char('A'))
        self.assertTrue(is_char('Z'))
        self.assertTrue(is_char('b'))
        self.assertTrue(is_char('B'))
        self.assertFalse(is_char(' '))
        self.assertFalse(is_char('#'))
        self.assertFalse(is_char('*'))

    def test_palindrome_permutation(self):
        self.assertTrue(palindrome_permutation('Tact Coa'))
        self.assertTrue(palindrome_permutation('jhsabckuj ahjsbckj'))
        self.assertTrue(palindrome_permutation('Able was I ere I saw Elba'))
        self.assertTrue(palindrome_permutation('no x in nixon'))
        self.assertTrue(palindrome_permutation('azAZ'))
        self.assertFalse(palindrome_permutation('So patient a nurse to nurse a patient so'))
        self.assertFalse(palindrome_permutation('Random Words'))
        self.assertFalse(palindrome_permutation('Not a Palindrome'))


if __name__ == '__main__':
    unittest.main()
