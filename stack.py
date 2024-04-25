class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return True if self.items else False
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if not self.is_empty:
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty:
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")
    
    def push(self, item):
        return self.items.append(item)

