class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, new_value):
        self.value = new_value

    def setNext(self, new_next):
        self.next = new_next

    def __str__(self):
        return ("{}".format(self.value))

    __repr__ = __str__


class Queue:
    # Do NOT modify the initializer
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.count

    def enqueue(self, item):
        if self.head == None:
            new_node = Node(item)
            self.head = new_node
            self.tail = self.head
        else:
            new_node = Node(item)
            self.tail.setNext(new_node)
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.head
        self.head = temp.next

        self.count -= 1
        return temp.value

    def printQueue(self):
        temp = self.head
        while (temp):
            print(temp.value, end=' ')
            temp = temp.next

q = Queue()
q.enqueue(10)
print(q.dequeue())
print(q.isEmpty())
print(q.dequeue())
q.enqueue(10)
q.enqueue(9)
q.enqueue(8)
q.enqueue(7)
q.enqueue(6)
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
q.enqueue(0)
print(q.size())
q.printQueue()
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(111)
q.enqueue(200)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q.size())
q.printQueue()






