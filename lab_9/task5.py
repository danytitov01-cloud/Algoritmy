class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def print_list(self):
        t = self.head
        while t != None:
            print(t.data, end=" ")
            t = t.next


l = List()
l.print_list()