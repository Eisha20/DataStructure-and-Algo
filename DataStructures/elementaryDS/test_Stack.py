import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def set_up_with_ints(self):
        """ initilazing a new stack with elements 1, 2, 3, 4"""

        self.test_stack = Stack()
        self.test_stack.push(1)
        self.test_stack.push(2)
        self.test_stack.push(3)
        self.test_stack.push(4)

    def set_up_empty_stack(self):
        self.test_stack = Stack()

    def test_pop_stack(self):
        """testing pop returns correct value"""
        self.set_up_with_ints()
        assert self.test_stack.pop() == 4
        assert self.test_stack.pop() == 3
        assert self.test_stack.pop() == 2
    

    def test_top_stack(self):
        """testing top method return the last inserted element """

        self.set_up_with_ints()
        assert self.test_stack.top() == 4
        assert self.test_stack.top() == 4

        self.test_stack.pop()
        assert self.test_stack.top() == 3

    def test_exception_on_empty_pop(self):
        self.set_up_empty_stack()
        with self.assertRaises(Exception):
            self.test_stack.pop()

    def test_exception_on_empty_top(self):
        self.set_up_empty_stack()
        with self.assertRaises(Exception):
            self.test_stack.top()

    def test_exception_on_empty_contains(self):
        self.set_up_empty_stack()
        with self.assertRaises(Exception):
            self.test_stack.contains()

    def test_isEmpty(self):
        self.set_up_empty_stack()
        assert self.test_stack.isEmpty() == True

        self.set_up_with_ints()
        assert self.test_stack.isEmpty() == False

    def test_contains(self):
        """testing contains method."""
        self.set_up_with_ints()
        assert self.test_stack.contains(1) == True
        assert self.test_stack.contains(4) == True
        assert self.test_stack.contains(5) == False
    
    def test_clear(self):
        """testing clear resets the stack"""
        self.set_up_with_ints()
        assert self.test_stack.isEmpty() == False
        self.test_stack.clear()
        assert self.test_stack.isEmpty() == True

if __name__ == '__main__':
    unittest.main()
