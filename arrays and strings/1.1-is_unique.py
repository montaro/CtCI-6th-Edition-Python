import unittest


def is_unique(word):
    if len(word) > 128:
        return False
    m = {}
    for c in word:
        if c in m.keys():
            return False
        else:
            m[c] = 1
    return True


def is_unique_2(word):
    if len(word) > 128:
        return False

    char_set = [False for _ in range(128)]
    for c in word:
        val = ord(c)
        if char_set[val]:
            return False
        else:
            char_set[val] = True

    return True


class Test(unittest.TestCase):
    dataT = ['abcd', 's4fad', '']
    dataF = ['23ds2', 'hb 627jh=j ()']

    def test_is_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

    def test_is_unique_2(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique_2(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique_2(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
