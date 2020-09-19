import unittest


class Node(object):
    next = None

    def __init__(self, d):
        self.data = d

    def append_to_tail(self, d):
        end = Node(d)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end

    def count(self):
        temp = self
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count


def delete_node(head, d):
    if head.data == d:
        return head.next
    while head.next is not None:
        if head.next.data == d:
            head.next = head.next.next
        head = head.next
    return head


class MyTestCase(unittest.TestCase):
    def test_linked_list(self):
        nono = Node(23)
        nono.append_to_tail(7)
        nono.append_to_tail(8)
        self.assertEqual(nono.data, 23)
        self.assertEqual(nono.next.data, 7)
        self.assertEqual(nono.next.next.data, 8)

    def test_delete_node(self):
        nono = Node(23)
        nono.append_to_tail(7)
        nono.append_to_tail(8)
        delete_node(nono, 7)
        self.assertEqual(nono.data, 23)
        self.assertEqual(nono.next.data, 8)

    def test_count(self):
        nono = Node(23)
        nono.append_to_tail(7)
        nono.append_to_tail(8)
        self.assertEqual(nono.count(), 3)


if __name__ == '__main__':
    unittest.main()
