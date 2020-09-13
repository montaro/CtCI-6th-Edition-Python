import unittest
from Chapter2 import LinkedList


def remove_dubs(head):
    if head is None:
        return

    current = head
    seen = {head.data}
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

    return head


def remove_dubs_no_buffer(head):
    if head is None:
        return

    current = head
    while current:
        runner = current
        while runner.next:
            if current.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head


class MyTestCase(unittest.TestCase):
    def test_remove_dubs(self):
        ll = LinkedList.Node(23)
        ll.append_to_tail(7)
        ll.append_to_tail(8)
        ll.append_to_tail(23)
        ll.append_to_tail(25)
        ll.append_to_tail(8)
        ll.append_to_tail(38)
        remove_dubs(ll)
        self.assertEqual(ll.data, 23)
        self.assertEqual(ll.next.data, 7)
        self.assertEqual(ll.next.next.data, 8)
        self.assertEqual(ll.next.next.next.data, 25)
        self.assertEqual(ll.next.next.next.next.data, 38)

    def test(self):
        ll = LinkedList.Node(23)
        ll.append_to_tail(7)
        ll.append_to_tail(8)
        ll.append_to_tail(23)
        ll.append_to_tail(25)
        ll.append_to_tail(8)
        ll.append_to_tail(38)
        remove_dubs_no_buffer(ll)
        self.assertEqual(ll.data, 23)
        self.assertEqual(ll.next.data, 7)
        self.assertEqual(ll.next.next.data, 8)
        self.assertEqual(ll.next.next.next.data, 25)
        self.assertEqual(ll.next.next.next.next.data, 38)


if __name__ == '__main__':
    unittest.main()
