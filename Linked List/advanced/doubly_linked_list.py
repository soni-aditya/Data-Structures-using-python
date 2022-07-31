class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        # change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        # move the head to point to the new node
        self.head = new_node

    # Given a node as prev_node, insert a new node after
    # the given node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return

        new_node = Node(new_data)

        # Make net of new node as next of prev node
        new_node.next = prev_node.next

        # Make prev_node as previous of new_node
        prev_node.next = new_node

        # Make prev_node ass previous of new_node
        new_node.prev = prev_node

        # Change previous of new_nodes's next node
        if new_node.next:
            new_node.next.prev = new_node

    # Given a reference to the head of DLL and integer,
    # appends a new node at the end
    def append(self, new_data):
        new_node = Node(new_data)

        # This new node is going to be the last node,
        # so make next of it as None
        # (It already is initialized as None)

        # If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return

        # Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # Change the next of last node
        last.next = new_node

        # Make last node as previous of new node
        new_node.prev = last

        return

    # This function prints contents of linked list
    # starting from the given node
    def printList(self, node):

        print("\nTraversal in forward direction")
        while node:
            print(" {}".format(node.data))
            last = node
            node = node.next

        print("\nTraversal in reverse direction")
        while last:
            print(" {}".format(last.data))
            last = last.prev


if __name__ == '__main__':
    llist = DoublyLinkedList()

    # Insert 6. So the list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning.
    # So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning.
    # So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end.
    # So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7.
    # So linked list becomes 1->7->8->6->4->None
    llist.insertAfter(llist.head.next, 8)

    print("Created DLL is: ")
    llist.printList(llist.head)
