import unittest
from Chapter2 import LinkedList


def palindrome(chars):
    word = ''
    while chars:
        word = word + chars.data
        chars = chars.next
    return word == ''.join(reversed(word))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        l1 = LinkedList.Node('r')
        l1.append_to_tail('a')
        l1.append_to_tail('c')
        l1.append_to_tail('e')
        l1.append_to_tail('c')
        l1.append_to_tail('a')
        l1.append_to_tail('r')
        self.assertTrue(palindrome(l1))
        l2 = LinkedList.Node('m')
        l2.append_to_tail('o')
        l2.append_to_tail('n')
        l2.append_to_tail('t')
        l2.append_to_tail('a')
        l2.append_to_tail('r')
        l2.append_to_tail('o')
        self.assertFalse(palindrome(l2))


if __name__ == '__main__':
    unittest.main()
