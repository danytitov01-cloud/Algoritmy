class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def add_last(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = n

    def count(self):
        t = self.head
        cnt = 0
        while t:
            cnt += 1
            t = t.next
        return cnt


l = List()
l.add_last(1)
l.add_last(2)
l.add_last(3)
l.add_last(4)
l.add_last(5)

print("Количество элементов:", l.count())  # 5