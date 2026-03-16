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

    def remove_first(self):
        if self.head:
            self.head = self.head.next


# Пример использования
l = List()
l.add_last(10)
l.add_last(20)
l.add_last(30)

print("До удаления:")
l.print_list()  # 10 20 30

l.remove_first()

print("После удаления:")
l.print_list()  # 20 30