class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def add_last(self, value):
        n = Node(value)

        if self.head == None:
            self.head = n
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = n


l = List()
l.add_last(10)
l.add_last(20)
l.add_last(30)
l.add_last(40)