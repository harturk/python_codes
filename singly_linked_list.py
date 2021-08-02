"""
My first steps into OOP was learning to manipulate a Singly Linked List. In the code bellow, it is showing how to
add elements at the end of list (works like append from static lists), add elements at the beginning, add elements in a n position (index)
"""

class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Method 1 to insert a value at the end of a linked list
    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return

        currNode = self.head
        while True:
            # If the current node is None, then the node will be inserted here
            if currNode.nextNode is None:
                currNode.nextNode = node
                break
            # If the current node is not None, the current node will be the next one
            # in order to keep travesing until find the tail
            currNode = currNode.nextNode

    # Method 2 to add at the end
    def addEnd(self, value):
        newNode = LinkedListNode(value)
        # If the list has no elements, it will return an error
        # unless the head have a value
        if self.head is None:
            self.head = newNode
            # This IF must have a return otherwise, it will be
            # in a infinity loop
            return
        currNode = self.head
        while currNode.nextNode is not None:
            currNode = currNode.nextNode
        currNode.nextNode = newNode

    # Method to print
    def printLinkedList(self):
        currNode = self.head
        if self.head is None:
            print("Linked list is empty")
        else:
            while currNode is not None:
                print(currNode.value, "->", end=" ")
                currNode = currNode.nextNode
            print("None")

    # Method to add at the beginning
    def addBegin(self, value):
        newNode = LinkedListNode(value)
        newNode.nextNode = self.head
        self.head = newNode


    def addNth(self, value, pos):
        i = 1
        newNode = LinkedListNode(value)
        currNode = self.head
        while True:
            if i == pos:
                break
            # This elif was added in order to not return an error in case
            # the position is out of bounds
            elif currNode.nextNode is None:
                print("Index out of bounds. Will be added as the last element")
                break
            else:
                currNode = currNode.nextNode
                i = i + 1
        backup = currNode.nextNode
        currNode.nextNode = newNode
        currNode.nextNode.nextNode = backup


ll = LinkedList()
ll.printLinkedList()
ll.addEnd(3)
ll.printLinkedList()
ll.addEnd(7)
ll.printLinkedList()
ll.addEnd(10)
ll.printLinkedList()
ll.addEnd(13)
ll.printLinkedList()

ll.addBegin(71)
ll.printLinkedList()

ll.insert(14)
ll.printLinkedList()

ll.insert(15)
ll.printLinkedList()

ll.addNth(2, 8)
ll.printLinkedList()
