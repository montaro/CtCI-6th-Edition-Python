import unittest
from Chapter2 import LinkedList


def loop_detection(head):
    refs = []
    while head:
        refs.append(head)
        if head.next in refs:
            return head.next
        head = head.next


class MyTestCase(unittest.TestCase):
    def test_loop_detection(self):
        a = LinkedList.Node(23)
        b = LinkedList.Node(88)
        c = LinkedList.Node(42)
        d = LinkedList.Node(99)
        e = LinkedList.Node(100)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = c
        self.assertTrue(c is loop_detection(a))


if __name__ == '__main__':
    unittest.main()
