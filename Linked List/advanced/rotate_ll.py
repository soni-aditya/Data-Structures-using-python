'''
Given a singly linked list, rotate the linked list counter-clockwise by k nodes. Where k is a given positive integer. For example, if the given linked list is 10->20->30->40->50->60 and k is 4, the list should be modified to 50->60->10->20->30->40. Assume that k is smaller than the count of nodes in a linked list.
'''

'''
To rotate a linked list by k, we can first make the linked list as circular and then moving k-1 steps forward from head node, making (k-1)th node’s next to null and make kth node as head.
'''


class Node:

    def __init__(self):

        self.data = 0
        self.next = None

# This function rotates a linked list
# counter-clockwise and updates the
# head. The function assumes that k is
# smaller than size of linked list.


def rotate(head_ref, k):

    if (k == 0):
        return

    # Let us understand the below
    # code for example k = 4 and
    # list = 10.20.30.40.50.60.
    current = head_ref

    # Traverse till the end.
    while (current.next != None):
        current = current.next

    current.next = head_ref
    current = head_ref

    # Traverse the linked list to k-1
    # position which will be last element
    # for rotated array.
    for i in range(k - 1):
        current = current.next

    # Update the head_ref and last
    # element pointer to None
    head_ref = current.next
    current.next = None
    return head_ref

# UTILITY FUNCTIONS
# Function to push a node


def push(head_ref, new_data):

    # Allocate node
    new_node = Node()

    # Put in the data
    new_node.data = new_data

    # Link the old list off
    # the new node
    new_node.next = (head_ref)

    # Move the head to point
    # to the new node
    (head_ref) = new_node
    return head_ref

# Function to print linked list


def printList(node):

    while (node != None):
        print(node.data, end=' ')
        node = node.next


if __name__ == '__main__':

    # Start with the empty list
    head = None

    # Create a list 10.20.30.40.50.60
    for i in range(60, 0, -10):
        head = push(head, i)

    print("Given linked list ")
    printList(head)
    head = rotate(head, 4)

    print("\nRotated Linked list ")
    printList(head)
