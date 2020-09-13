import unittest
from Chapter2 import LinkedList


def kth_to_last(head, k):
    runner = current = head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


class MyTestCase(unittest.TestCase):
    def test_kth_to_last(self):
        ll = LinkedList.Node(23)
        ll.append_to_tail(7)
        ll.append_to_tail(8)
        ll.append_to_tail(23)
        ll.append_to_tail(25)
        ll.append_to_tail(8)
        ll.append_to_tail(38)
        kth = kth_to_last(ll, 3)
        self.assertEqual(kth.data, 25)
        self.assertEqual(kth.next.data, 8)
        self.assertEqual(kth.next.next.data, 38)


if __name__ == '__main__':
    unittest.main()
