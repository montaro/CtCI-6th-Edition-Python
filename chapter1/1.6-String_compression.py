import unittest


def string_compress(string):
    compressed = []
    c = string[0]
    n = 1
    for i in range(1, len(string)):
        if string[i] == c:
            n = n + 1
        else:
            compressed.append(c)
            compressed.append(str(n))
            c = string[i]
            n = 1
    compressed.append(c)
    compressed.append(str(n))
    compressed = ''.join(compressed)
    return min(string, compressed, key=len)


class MyTestCase(unittest.TestCase):
    def test_string_compress(self):
        self.assertEqual(string_compress('aabcccccaaa'), 'a2b1c5a3')
        self.assertEqual(string_compress('abcdef'), 'abcdef')


if __name__ == '__main__':
    unittest.main()
