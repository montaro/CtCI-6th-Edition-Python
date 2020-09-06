import unittest


def one_away(s1, s2):
    if s1 == s2:
        return True
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    if len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    if len(s2) + 1 == len(s1):
        return one_edit_insert(s2, s1)


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if not edited:
                edited = True
            else:
                return False
    return True


def one_edit_insert(s1, s2):
    edited = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            s1 = s1[:i] + s2[i] + s1[i:]
            edited = True
            break
    if not edited:
        s1 = s1 + s2[-1]
    return s1 == s2


class MyTestCase(unittest.TestCase):
    def test_one_away(self):
        self.assertTrue(one_away('ahmed', 'ahmed'))
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('pales', 'pale'))
        self.assertTrue(one_away('pale', 'bale'))
        self.assertTrue(one_away('paleabc', 'pleabc'))
        self.assertFalse(one_away('pale', 'ble'))
        self.assertTrue(one_away('a', 'b'))
        self.assertTrue(one_away('', 'd'))
        self.assertTrue(one_away('d', 'de'))
        self.assertTrue(one_away('pale', 'pale'))
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('ple', 'pale'))
        self.assertTrue(one_away('pale', 'bale'))
        self.assertFalse(one_away('pale', 'bake'))
        self.assertFalse(one_away('pale', 'pse'))
        self.assertTrue(one_away('ples', 'pales'))
        self.assertFalse(one_away('pale', 'pas'))
        self.assertFalse(one_away('pas', 'pale'))
        self.assertTrue(one_away('pale', 'pkle'))
        self.assertFalse(one_away('pkle', 'pable'))
        self.assertFalse(one_away('pal', 'palks'))
        self.assertFalse(one_away('palks', 'pal'))


if __name__ == '__main__':
    unittest.main()
