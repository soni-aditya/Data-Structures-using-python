class Node:

    # Function to initialise the node object
    def __init__(self, data) -> None:
        self.data = data    # Assign data
        self.next = None    # Initialize next as null

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''


    #inserting first node
    linked_list.head = Node(1)

    # inserting second node
    second = Node(2)
    linked_list.head.next = second

    '''
    Now next of first Node refers to second.  So they
    both are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''

    # inserting third node
    third = Node(3)
    second.next = third

    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''