# Stats

| Time Complexity      | Worst Case  | Best Case |
| -------------------- | ----------- | --------- |
| Search / Traversal   | O(n )       | O(n)      |
| Insert               | O(1)        | O(1)      |
| Deletion             | O(1)        | O(1)      |


| Space Complexity      | Worst Case  | 
| -------------------- | ----------- | 
| Search / Traversal   | O(n )       |
| Insert               | O(1)        | 
| Deletion             | O(1)  if you go with loops <br> O(n) if you go with recursion |


### The various types of linked lists are as follows:

**Singly Linked List:** It is the most basic linked list in which traversal is unidirectional i.e. from the head node to the last node.
**Doubly Linked List:** In this linked list, traversal can be done in both ways, and hence it requires an extra pointer.
**Circular Linked List:** This linked list is unidirectional but in this list, the last node points to the first i.e. the head node and hence it becomes circular in nature.
**Circular Doubly Linked List:** The circular doubly linked list is a combination of the doubly linked list and the circular linked list. It means that this linked list is bidirectional and contains two pointers and the last pointer points to the first pointer.


### Advantages of Linked Lists:
- Insertion and deletion in linked lists are very efficient.
- Linked list can be expanded in constant time.
- For implementation of stacks and queues and for representation of trees and graphs.
- Linked lists are used for dynamic memory allocation which means effective memory utilization hence, no memory wastage.

### Disadvantages of Linked Lists:
- Use of pointers is more in linked lists hence, complex and requires more memory.
- Searching an element is costly and requires O(n) time complexity.
- Traversing is more time consuming and reverse traversing is not possible in singly linked lists.
- Random access is not possible due to dynamic memory allocation.


### Applications of Linked Lists:
- Linked Lists are used to implement stacks and queues.
- It is used for the various representations of trees and graphs.
- It is used in dynamic memory allocation( linked list of free blocks).
- It is used for representing sparse matrices.
- It is used for the manipulation of polynomials.
- It is also used for performing arithmetic operations on long integers.
- It is used for finding paths in networks.