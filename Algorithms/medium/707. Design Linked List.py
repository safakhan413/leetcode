"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        # print('Im the val', self.val)
        return f"{self.val}"

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        i = 0
        while i < index:
            current = current.next
            i = i+1
        # print
        return current.val

    def addAtHead(self, val: int) -> None:
        current = self.head
        new_head = Node(val)        
        
        # make new heads next the current
        new_head.next = current

        # declare new head to be new self.head
        self.head = new_head
        self.size = self.size + 1

    def addAtTail(self, val: int) -> None:
        tail_node = Node(val)
        if self.head is None:
            # self.addAtHead(tail_node)
            self.head = tail_node
            self.size +=1
        
        else:

            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = tail_node
            self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            print('Invalid index for adding element')
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            newNode = Node(val)
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            print('Invalid index for deleting element')
            return
        
        if index == 0:  # Special case: deleting the head
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def print(self):
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next

#    print()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.print()

# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(2)
obj.addAtHead(3)
obj.addAtTail(5)
obj.addAtTail(6)
obj.addAtIndex(2,7)
# obj.deleteAtIndex(2)


print(obj.print())
print('Im getting', obj.get(0))
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)