

class Stack:
    
    def __init__ (self):
        self.index = 0
        self.internalStack = []
    
    def push(self, elem):
        self.internalStack += [elem]
    
    def pop(self):
        if self.internalStack == []:
            raise Exception('Cannot pop an empty stack')
        elem = self.internalStack[-1]
        self.internalStack = self.internalStack[:-1]
        return elem

    def top(self):
        if self.internalStack == []:
            raise Exception('Cannot return top of an empty stack')
        return self.internalStack[-1]
    
    def isEmpty(self):
        return self.internalStack == []

    def contains(self, elem):
        if self.internalStack == []:
            raise Exception('The stack is empty')
        return elem in self.internalStack

    def clear(self):
        self.internalStack = []