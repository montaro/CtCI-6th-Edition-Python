import unittest
from collections import Counter


def check_permutation(word1, word2):
    if len(word1) != len(word2):
        return False

    word1 = sorted(word1)
    word2 = sorted(word2)

    if word1 == word2:
        return True
    else:
        return False


def check_permutation_2(word1, word2):
    if len(word1) != len(word2):
        return False
    c1 = Counter(word1)
    c2 = Counter(word2)
    return c1 == c2


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_check_permutation(self):
        # true check
        for test_strings in self.dataT:
            self.assertTrue(check_permutation(*test_strings))
        # false check
        for test_strings in self.dataF:
            self.assertFalse(check_permutation(*test_strings))

    def test_check_permutation_2(self):
        # true check
        for test_strings in self.dataT:
            self.assertTrue(check_permutation_2(*test_strings))
        # false check
        for test_strings in self.dataF:
            self.assertFalse(check_permutation_2(*test_strings))


if __name__ == "__main__":
    unittest.main()
