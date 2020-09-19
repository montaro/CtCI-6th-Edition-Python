import unittest
from Chapter2 import LinkedList


def intersection(l1, l2):
    ll1 = l1
    while ll1:
        ll2 = l2
        while ll2:
            if ll1 is ll2:
                return ll1
            else:
                ll2 = ll2.next
        ll1 = ll1.next


def intersection2(l1, l2):
    if l1.tail() is not l2.tail():
        return None

    l1_count = l1.count()
    l2_count = l2.count()
    longer = l1 if l1_count > l2_count else l2
    shorter = l1 if l1_count < l2_count else l2
    diff = l1_count - l2_count
    for _ in range(diff):
        longer = longer.next
    while longer is not shorter:
        longer = longer.next
        shorter = shorter.next
    return longer


class MyTestCase(unittest.TestCase):
    def test_intersection(self):
        intersection_node = LinkedList.Node(23)
        l1 = LinkedList.Node(88)
        l1.next = LinkedList.Node(7)
        l1.next.next = LinkedList.Node(3)
        l1.next.next.next = intersection_node
        l1.append_to_tail(42)
        l2 = LinkedList.Node(8)
        l2.next = LinkedList.Node(77)
        l2.next.next = intersection_node
        l2.append_to_tail(24)
        l2.append_to_tail(15)
        l2.append_to_tail(60)
        l2.append_to_tail(39)
        self.assertEqual(intersection_node, intersection(l1, l2))

    def test_intersection2(self):
        intersection_node = LinkedList.Node(23)
        l1 = LinkedList.Node(88)
        l1.next = LinkedList.Node(7)
        l1.next.next = LinkedList.Node(3)
        l1.next.next.next = intersection_node
        l1.append_to_tail(42)
        l2 = LinkedList.Node(8)
        l2.next = LinkedList.Node(77)
        l2.next.next = intersection_node
        l2.append_to_tail(24)
        l2.append_to_tail(15)
        l2.append_to_tail(60)
        l2.append_to_tail(39)
        self.assertEqual(intersection_node, intersection2(l1, l2))

        x1 = LinkedList.Node(23)
        x1.append_to_tail(88)
        x2 = LinkedList.Node(42)
        x2.append_to_tail(99)
        self.assertIsNone(intersection2(x1, x2))


if __name__ == '__main__':
    unittest.main()
