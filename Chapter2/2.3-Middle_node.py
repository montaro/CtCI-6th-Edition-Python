import unittest
from Chapter2 import LinkedList


def middle_node(node):
    node.data = node.next.data
    node.next = node.next.next
    return node


class MyTestCase(unittest.TestCase):
    def test_middle_node(self):
        ll = LinkedList.Node(23)
        ll.append_to_tail(7)
        ll.append_to_tail(8)
        ll.append_to_tail(23)
        ll.append_to_tail(25)
        ll.append_to_tail(8)
        ll.append_to_tail(38)
        ll = middle_node(ll)
        self.assertEqual(ll.data, 7)
        self.assertEqual(ll.next.data, 8)
        self.assertEqual(ll.next.next.data, 23)
        self.assertEqual(ll.next.next.next.data, 25)
        self.assertEqual(ll.next.next.next.next.data, 8)
        self.assertEqual(ll.next.next.next.next.next.data, 38)


if __name__ == '__main__':
    unittest.main()
