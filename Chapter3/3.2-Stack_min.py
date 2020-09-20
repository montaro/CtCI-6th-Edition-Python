import unittest
import sys


class StackNodeWithMin(object):
    def __init__(self, data, mini):
        self.data = data
        self.next = None
        self.mini = mini


class IsEmptyException(Exception):
    pass


class StackWithMin(object):
    def __init__(self):
        self._top_ = None

    def pop(self):
        if self._top_:
            value = self._top_.data
            self._top_ = self._top_.next
            return value
        raise IsEmptyException()

    def push(self, data):
        new_mini = min(data, self.min())
        t = StackNodeWithMin(data, new_mini)
        t.next = self._top_
        self._top_ = t

    def min(self):
        if self.is_empty():
            return sys.maxsize
        return self.peek().mini

    def peek(self):
        if self._top_:
            return self._top_
        raise IsEmptyException()

    def is_empty(self):
        return self._top_ is None


class MyTestCase(unittest.TestCase):
    def test_stack_node_with_min(self):
        node = StackNodeWithMin(23, 3)
        self.assertEqual(node.data, 23)
        self.assertIsNone(node.next)
        self.assertEqual(node.mini, 3)

    def test_stack(self):
        stack = StackWithMin()
        with self.assertRaises(IsEmptyException):
            stack.peek()
        with self.assertRaises(IsEmptyException):
            stack.pop()
        self.assertTrue(stack.is_empty())
        stack.push(23)
        self.assertEqual(stack.peek().data, 23)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.min(), 23)
        self.assertEqual(stack.pop(), 23)
        self.assertEqual(stack.min(), sys.maxsize)
        stack.push(42)
        self.assertEqual(stack.min(), 42)
        stack.push(88)
        self.assertEqual(stack.min(), 42)
        stack.push(36)
        self.assertEqual(stack.min(), 36)
        self.assertEqual(stack.peek().data, 36)
        self.assertEqual(stack.pop(), 36)
        self.assertEqual(stack.peek().data, 88)


if __name__ == '__main__':
    unittest.main()
