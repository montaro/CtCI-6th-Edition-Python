import unittest


def urlify(url, length):
    for i in range(length):
        if url[i] == ' ':
            url[i + 3:] = url[i + 1: len(url) - 2]
            url[i] = '%'
            url[i + 1] = '2'
            url[i + 2] = '0'
    return url


class MyTestCase(unittest.TestCase):
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
