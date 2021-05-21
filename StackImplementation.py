### LAB #10 due 03/30 at 11:59 pm
# Submission Instructions
#  file name: LAB10.py
#  Do NOT change any function name

#### COLLABORATION STATEMENT:
####

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


class Stack:
    def __init__(self):
        self.top = None  # Do NOT modify this line
        #self.count = 0

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def size(self):
        count = 0
        temp = self.top
        while temp:
            #print(temp.getValue())
            temp = temp.getNext()
            count += 1
        return count


    def push(self, item):
        temp = Node(item)
        temp.next = self.top
        self.top = temp
        #self.count += 1

    def pop(self):
        if self.isEmpty():
            return None
        temp = self.top
        last = temp.value
        self.top = self.top.getNext()
        #self.count -= 1
        return last

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.value

    def printStack(self):

        temp = self.top
        while temp:
            print(temp.getValue())
            temp = temp.getNext()



s = Stack()
s.pop()
