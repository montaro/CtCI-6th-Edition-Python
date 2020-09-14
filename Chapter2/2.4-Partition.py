import unittest
from Chapter2 import LinkedList


def partition(head, x):
    current = head
    before_start = None
    before_end = None
    after_start = None
    after_end = None
    while current:
        if current.data < x:
            if before_start is None:
                before_start = current
                before_end = before_start
            else:
                before_end.next = current
                before_end = current
        else:
            if after_start is None:
                after_start = current
                after_end = after_start
            else:
                after_end.next = current
                after_end = current
        current = current.next

    if before_start is None:
        return after_start

    # merge the two lists
    before_end.next = after_start
    return before_start


class MyTestCase(unittest.TestCase):
    def test_partition(self):
        ll = LinkedList.Node(23)
        ll.append_to_tail(7)
        ll.append_to_tail(8)
        ll.append_to_tail(23)
        ll.append_to_tail(25)
        ll.append_to_tail(8)
        ll.append_to_tail(38)
        ll = partition(ll, 23)
        self.assertEqual(ll.data, 7)
        self.assertEqual(ll.next.data, 8)
        self.assertEqual(ll.next.next.data, 8)
        self.assertEqual(ll.next.next.next.data, 23)
        self.assertEqual(ll.next.next.next.next.data, 23)
        self.assertEqual(ll.next.next.next.next.next.data, 25)
        self.assertEqual(ll.next.next.next.next.next.next.data, 38)


if __name__ == '__main__':
    unittest.main()
