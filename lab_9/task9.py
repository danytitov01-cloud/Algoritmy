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

    def print_list(self):
        t = self.head
        while t:
            print(t.data, end=" ")
            t = t.next
        print()


l = List()

print("Введите 5 чисел:")
for i in range(5):
    num = int(input())
    l.add_last(num)

print("Список:")
l.print_list()