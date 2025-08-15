# Data Structures

#### 1. Stack

Based on Last In, First Out (LIFO) arrangement, new elements are inserted at top of the stack one at the time and user can delete the top element of the stack one at time.

#### 2. Queue

Based on First In, First Out (FIFO) arrangement, new element are insert at rear/ last and we can delete the first element in front of the list one at time.

#### 3. Linked List

Each element in a linked list is call node, a node contain of data and next attributes \[ Data : Next ]. next hold another node and so on. we track the head element of the linked list and perform insertion and deletion operations. we traversing the list one by one by it's data a→b→c.

#### 4. Doubly Linked List

Similar to linked list, each elements in this doubly linked list is node, unlike single linked list, this node contain previous, data and next attributes in it's node \[Previous: Data : Next]. We track the first element as head and perform add or delete operation based on head element. we traversing through the each element one by one with help of assigning the iterating current node.

#### 5. Circular Linked List

This is more like Singly Linked List, Each node contain Data : Next pairs. Unlike Linked List, we keep track of last element of the list, this is more useful to insert or delete the last element, for example in linked list, we have to traversing element from first to last, but in CLL we know the reference of last value and insert directly at end of the list. and Last : Next hold the head of the element node we easy determine and perform insertion and deletion operation.