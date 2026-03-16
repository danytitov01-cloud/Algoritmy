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

    def remove_value(self, value):
        t = self.head
        if t is None:
            return
        if t.data == value:
            self.head = t.next
            return
        while t.next:
            if t.next.data == value:
                t.next = t.next.next
                return
            t = t.next

    def insert_after(self, target, value):
        t = self.head
        while t:
            if t.data == target:
                n = Node(value)
                n.next = t.next
                t.next = n
                return
            t = t.next


l = List()
for num in [10, 20, 30, 40, 50]:
    l.add_last(num)

print("Начальный список:")
l.print_list()  # 10 20 30 40 50

val_to_remove = int(input("Введите значение для удаления: "))
l.remove_value(val_to_remove)

target = int(input("После какого значения вставить новый элемент? "))
new_val = int(input("Введите новое значение для вставки: "))
l.insert_after(target, new_val)

print("Итоговый список:")
l.print_list()