from collections import deque
from random import random


def print_table(table):
    for x in range(0, rows):
        for y in range(0, cols):
            print(table[x][y], end='')
        print()


rows, cols = 10, 10
table = [['G' if random() < 0.3 else 'W' for col in range(cols)] for row in range(rows)]
# todo:нужен другой способ инициализации таблицы
print_table(table)


def get_next_nodes_coordinates(x, y):
    def check_next_node_coordinates(x, y):
        return 0 <= x < rows and 0 <= y < cols and (table[x][y] != 'G')

    coordinates_difference = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(x + dif_x, y + dif_y) for dif_x, dif_y in coordinates_difference
            if check_next_node_coordinates(x + dif_x, y + dif_y)]


cells_to_visit = {}
for x, row in enumerate(table):
    for y, col in enumerate(row):
        if col == 'W':
            cells_to_visit[(x, y)] = cells_to_visit.get((x, y), []) + get_next_nodes_coordinates(x, y)

start = (0, 0)
goal = (5, 5)


# todo: goal должен быть водой - обработать ситуацию


def find_path(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return visited


visited = find_path(start, goal, cells_to_visit)

visited_node = goal
while visited_node is not None and visited_node in visited:
    visited_node = visited[visited_node]
    if visited_node:
        table[visited_node[0]][visited_node[1]] = '-'

print_table(table)
