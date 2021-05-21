class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, new_value):
        self.value = new_value

    def setNext(self, new_next):
        self.next = new_next

    def getPrevious(self):
        return self.prev

    def setPrevious(self, new_prev):
        self.prev = new_prev

    def __str__(self):
        return ("{}".format(self.value))

    __repr__ = __str__


class DoublyLinkedList:
    # Do NOT modify the constructor
    def __init__(self):
        self.head = None

    def addFirst(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode

    def addLast(self, value):
        pass

    def addBefore(self, pnode_value, value):
        pass
    def addAfter(self, pnode_value, value):
       pass

    def printDLL(self):
        temp = self.head
        print("\nTraversal Head to Tail")
        while temp:
            print(temp.getValue(), end=' ')
            last = temp
            temp = temp.getNext()

        print("\nTraversal Tail to Head")
        while (last is not None):
            print(last.getValue(), end=' ')
            last = last.prev

    def getNode(self, value):
        current = self.head
        found = False
        while current != None and not found:
            if current.getValue() == value:
                found = True
                return current
            else:
                current = current.getNext()
        return
dll = DoublyLinkedList()
dll.addFirst(2)
dll.addFirst(3)
dll.addFirst(4)
dll.addFirst(9)

dll.printDLL()