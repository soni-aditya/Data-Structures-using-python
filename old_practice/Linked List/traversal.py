class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    linked_list = LinkedList()

    first = Node(1)
    second = Node("Second Node Data")
    third = Node(3)

    linked_list.head = first
    first.next = second
    second.next = third

    linked_list.printList()
