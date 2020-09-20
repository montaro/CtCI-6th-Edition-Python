import unittest


class StackNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class IsEmptyException(Exception):
    pass


class Stack(object):
    def __init__(self):
        self._top_ = None

    def pop(self):
        if self._top_:
            value = self._top_.data
            self._top_ = self._top_.next
            return value
        raise IsEmptyException()

    def push(self, data):
        t = StackNode(data)
        t.next = self._top_
        self._top_ = t

    def peek(self):
        if self._top_:
            return self._top_
        raise IsEmptyException()

    def is_empty(self):
        return self._top_ is None


class MyTestCase(unittest.TestCase):
    def test_stack_node(self):
        node = StackNode(23)
        self.assertEqual(node.data, 23)
        self.assertIsNone(node.next)

    def test_stack(self):
        stack = Stack()
        with self.assertRaises(IsEmptyException):
            stack.peek()
        with self.assertRaises(IsEmptyException):
            stack.pop()
        self.assertTrue(stack.is_empty())
        stack.push(23)
        self.assertEqual(stack.peek().data, 23)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), 23)
        stack.push(42)
        stack.push(88)
        stack.push(36)
        self.assertEqual(stack.peek().data, 36)
        self.assertEqual(stack.pop(), 36)
        self.assertEqual(stack.peek().data, 88)


if __name__ == '__main__':
    unittest.main()
