import unittest


class QueueNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class NoSuchElementException(Exception):
    pass


class Queue(object):
    def __init__(self):
        self._first_ = None
        self._last_ = None

    def add(self, data):
        node = QueueNode(data)
        if self._last_:
            self._last_.next = node
        self._last_ = node
        if not self._first_:
            self._first_ = self._last_

    def remove(self):
        if not self._first_:
            raise NoSuchElementException()
        node = QueueNode(self._first_.data)
        self._first_ = self._first_.next
        if not self._first_:
            self._last_ = None
        return node.data

    def peek(self):
        if not self._first_:
            raise NoSuchElementException()
        return self._first_.data

    def is_empty(self):
        return self._first_ is None


class MyTestCase(unittest.TestCase):
    def test_queue_node(self):
        node = QueueNode(23)
        self.assertEqual(node.data, 23)
        self.assertIsNone(node.next)

    def test_queue(self):
        queue = Queue()
        with self.assertRaises(NoSuchElementException):
            queue.remove()
        with self.assertRaises(NoSuchElementException):
            queue.peek()
        self.assertTrue(queue.is_empty())
        queue.add(23)
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.peek(), 23)
        self.assertEqual(queue.remove(), 23)
        with self.assertRaises(NoSuchElementException):
            queue.remove()
        with self.assertRaises(NoSuchElementException):
            queue.peek()
        queue.add(42)
        queue.add(88)
        queue.add(36)
        queue.add(73)
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.peek(), 42)
        self.assertEqual(queue.remove(), 42)
        queue.add(7)
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.peek(), 88)
        self.assertEqual(queue.remove(), 88)


if __name__ == '__main__':
    unittest.main()
