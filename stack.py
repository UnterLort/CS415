class Stack:
    pass
# Defining a class

    def __init__(self):
        self.items = []
    # Defining the constructor method

    def push(self, value):
        self.items.append(value)
    # Defining a method push which takes a value as input and adds it to the items

    def pop(self):
        if len(self.items) == 0:
            raise Exception("Stack is empty")
        return self.items.pop()
    # Defining a method pop which returns the last item from the items without removing it.
    # If the list is empty, it raises an exception.

    def top(self):
        if len(self.items) == 0:
            raise Exception("Stack is empty")
        return self.items[-1]
    # Defining a method top which returns the last item from the items without removing it.
    # If the list is empty, it raises an exception.

    def __len__(self):
        return len(self.items)
    # Defining the __len__ method which returns the length items

    def __getitem__(self, index):
        if index < -len(self.items) or index >= len(self.items):
            raise IndexError("Index out of bounds")
        return self.items[index]
    # Defining the __getitem__ method which allows indexing of items.
    # It raises an IndexError if the index is out of bounds.

    def __iter__(self):
        return iter(self.items)
    # Defining the __iter__ method which returns an iterator for the items.


    def __repr__(self):
        return repr(self.items)
    # Defining the __repr__ method which returns a str of the items
