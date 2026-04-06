from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

print("Задача 1:", graph)

graph['F'] = ['A', 'E']
graph['A'].append('F')

print("\nЗадача 2:", graph)


def get_neighbors(graph, node):
    return graph.get(node, [])

print("\nЗадача 3:", get_neighbors(graph, 'A'))


def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


print("\nЗадача 4 (DFS рекурсивно):")
print(dfs_recursive(graph, 'A'))


def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            stack.extend(reversed(graph[node]))

    return visited


print("\nЗадача 5 (DFS стек):")
print(dfs_stack(graph, 'A'))


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

    return visited


print("\nЗадача 6 (BFS):")
print(bfs(graph, 'A'))


def traverse(graph, start):
    visited = bfs(graph, start)
    print("\nЗадача 7:")
    print("Старт:", start)
    print("Порядок обхода:", visited)


traverse(graph, 'A')


def has_path(graph, start, end):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node == end:
            return True

        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

    return False


print("\nЗадача 8:")
print(has_path(graph, 'A', 'E'))


def reachable_count(graph, start):
    return len(bfs(graph, start))


print("\nЗадача 9:")
print(reachable_count(graph, 'A'))


def shortest_path(graph, start, end):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                queue.append(path + [neighbor])

    return None


print("\nЗадача 10:")
print(shortest_path(graph, 'A', 'E'))

# Что такое граф?
# Граф это структура данных, состоящая из вершин (узлов) и рёбер (связей между ними).

# Чем DFS отличается от BFS?
# DFS идёт вглубь (как можно дальше по одной ветке), BFS вширь (по уровням).

# Почему нужно хранить visited?
# Чтобы не зациклиться и не проходить одни и те же вершины повторно.

# Как представляется граф в Python?
# Обычно в виде словаря: ключ вершина, значение список соседей.

# Какой алгоритм используется для поиска кратчайшего пути?
# В невзвешенном графе BFS.