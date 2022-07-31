class Node:

    # Function to initialise the node object
    def __init__(self, data) -> None:
        self.data = data    # Assign data
        self.next = None    # Initialize next as null


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # insert data at the starting of the linked list
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    '''
    Given a reference to the head of a list and a value, delete the first occurrence of value in linked list
    '''

    def deleteNode(self, value):
        temp = self.head

        # If head node itself holds the value to be deleted
        if temp is not None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return

        # Search for the value to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        prev = None
        while temp is not None:
            if temp.data == value:
                break

            prev = temp
            temp = temp.next

        # if value is not present in the linked list
        if temp is None:
            print("The value to be deleted is not present in the linked list")
            return

        # unlink the value to be deleted
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    linked_list.push(5)
    linked_list.push(6)

    print(f"Created Linked list: \n{linked_list.printList()}")
    linked_list.deleteNode(3)
    print(f"After removal of 3: \n{linked_list.printList()}")
