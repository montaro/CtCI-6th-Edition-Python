import unittest
from Chapter2 import LinkedList


def sum_lists(l1, l2):
    factor = 1
    n1 = 0
    while l1:
        s = l1.data * factor
        n1 = n1 + s
        factor = factor * 10
        l1 = l1.next
    factor = 1
    n2 = 0
    while l2:
        s = l2.data * factor
        n2 = n2 + s
        factor = factor * 10
        l2 = l2.next
    n = n1 + n2
    sum_of_lists = None
    while n:
        value = n % 10
        if not sum_of_lists:
            sum_of_lists = LinkedList.Node(value)
        else:
            sum_of_lists.append_to_tail(value)
        n = n - value
        n = n / 10
    return sum_of_lists


class MyTestCase(unittest.TestCase):
    def test_sum_lists(self):
        l1 = LinkedList.Node(7)
        l1.append_to_tail(1)
        l1.append_to_tail(6)
        l2 = LinkedList.Node(5)
        l2.append_to_tail(9)
        l2.append_to_tail(2)
        sum_of_lists = sum_lists(l1, l2)
        self.assertEqual(sum_of_lists.data, 2)
        self.assertEqual(sum_of_lists.next.data, 1)
        self.assertEqual(sum_of_lists.next.next.data, 9)


if __name__ == '__main__':
    unittest.main()
