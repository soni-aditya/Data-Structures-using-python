class Node:

    # Function to initialise the node object
    def __init__(self, data) -> None:
        self.data = data    # Assign data
        self.next = None    # Initialize next as null


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # function to insert new node at the begining
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node

    # function to insert a new node after a given previous_node
    def insertAfter(self, previous_node, data):
        if previous_node is None:
            print("Given previous node is not present in the Linkedin List")
            return

        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    # function to inesrt a new node at the end of the linked list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        # traversing the list till the end
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    linked_list = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    linked_list.append(6)
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    linked_list.push(7)
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    linked_list.push(1)
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    linked_list.append(4)
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    linked_list.insertAfter(linked_list.head.next, 8)

    print('Created linked list is: ')
    linked_list.printList()
