# Задача 1
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Задача 2
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.left = Node(25)
root.right.right = Node(35)

print("Корень:", root.data)
print("Левый:", root.left.data)
print("Правый:", root.right.data)

# Задача 3
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

# Задача 4
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# Задача 5
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

# Задача 6
def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# Задача 7
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

# Задача 8
def count_leaves(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

# Задача 9
def search(node, value):
    if not node:
        return False
    if node.data == value:
        return True
    return search(node.left, value) or search(node.right, value)

# Задача 10
print("\nPreorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)

print("\nКоличество узлов:", count_nodes(root))
print("Количество листьев:", count_leaves(root))
print("Высота дерева:", height(root))

print("Поиск 15:", search(root, 15))
print("Поиск 100:", search(root, 100))