class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def search(self, value):
        t = self.head
        while t != None:
            if t.data == value:
                return True
            t = t.next
        return False


l = List()
print(l.search(10))