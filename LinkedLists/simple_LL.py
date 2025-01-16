class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node = None
        if value is not None:
            node = Node(value)
        self.head = node
        self.tail = node
        length = 1 if value is not None else 0
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        # else:
            # for self.head.next is not None:
                # self.head = 