import unittest


class EmptyStack(Exception):
    pass


class FullStack(Exception):
    pass


class FixedMultiStack(object):
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.number_of_stacks = 3
        self.sizes = [0] * self.number_of_stacks
        self.values = [0] * self.number_of_stacks * stack_size

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise FullStack()
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise EmptyStack()
        top_index = self.index_of_top(stack_num)
        value = self.values[top_index]
        self.values[top_index] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise EmptyStack()
        return self.values[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1


class MyTestCase(unittest.TestCase):
    def test_fixed_multi_stack(self):
        fms = FixedMultiStack(7)
        self.assertTrue(fms.is_empty(0))
        self.assertTrue(fms.is_empty(1))
        self.assertTrue(fms.is_empty(2))
        self.assertFalse(fms.is_full(0))
        self.assertFalse(fms.is_full(1))
        self.assertFalse(fms.is_full(2))
        with self.assertRaises(EmptyStack):
            fms.peek(0)
        with self.assertRaises(EmptyStack):
            fms.peek(1)
        with self.assertRaises(EmptyStack):
            fms.peek(2)
        with self.assertRaises(EmptyStack):
            fms.pop(0)
        with self.assertRaises(EmptyStack):
            fms.pop(1)
        with self.assertRaises(EmptyStack):
            fms.pop(2)
        fms.push(0, 0)
        fms.push(0, 1)
        fms.push(0, 2)
        fms.push(0, 3)
        fms.push(1, 7)
        fms.push(1, 8)
        fms.push(2, 14)
        fms.push(2, 15)
        fms.push(2, 16)
        self.assertEqual(fms.index_of_top(0), 3)
        self.assertEqual(fms.index_of_top(1), 8)
        self.assertEqual(fms.index_of_top(2), 16)
        self.assertEqual(fms.peek(0), 3)
        self.assertEqual(fms.peek(1), 8)
        self.assertEqual(fms.peek(2), 16)
        self.assertFalse(fms.is_full(0))
        self.assertFalse(fms.is_full(1))
        self.assertFalse(fms.is_full(2))
        self.assertFalse(fms.is_empty(0))
        self.assertFalse(fms.is_empty(1))
        self.assertFalse(fms.is_empty(2))
        self.assertEqual(fms.pop(0), 3)
        self.assertEqual(fms.pop(0), 2)
        self.assertEqual(fms.pop(1), 8)
        self.assertEqual(fms.pop(1), 7)
        self.assertEqual(fms.pop(2), 16)
        self.assertEqual(fms.pop(2), 15)
        self.assertFalse(fms.is_empty(0))
        self.assertTrue(fms.is_empty(1))
        self.assertFalse(fms.is_empty(2))
        self.assertEqual(fms.peek(0), 1)
        with self.assertRaises(EmptyStack):
            fms.peek(1)
        self.assertEqual(fms.peek(2), 14)


if __name__ == '__main__':
    unittest.main()
