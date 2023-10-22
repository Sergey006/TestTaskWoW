from collections import deque
from random import random
from typing import Any

from second_task.models.colors import Colors


class PathFinder:
    __ground_cell_symbol = f'{Colors.GREEN.value}*{Colors.END_COLOR.value}'
    __water_cell_symbol = f'{Colors.CYAN.value}.{Colors.END_COLOR.value}'
    __visited_cell_symbol = f'{Colors.RED.value}-{Colors.END_COLOR.value}'
    __finish_cell_symbol = f'{Colors.RED.value}F{Colors.END_COLOR.value}'
    __start_cell_symbol = f'{Colors.RED.value}S{Colors.END_COLOR.value}'

    def __init__(self, rows_qty, cols_qty, start_xy, end_xy):
        self.__field = [
            [self.__ground_cell_symbol if random() < 0.1 else self.__water_cell_symbol for _ in range(cols_qty)] for _
            in
            range(rows_qty)]
        self.__rows_number, self.__cols_number = rows_qty, cols_qty
        self.__start = start_xy
        self.__end = end_xy
        if self.__field[self.__start[0]][self.__start[1]] == self.__ground_cell_symbol:
            self.__field[self.__start[0]][self.__start[1]] = self.__water_cell_symbol
        if self.__field[self.__end[0]][self.__end[1]] == self.__ground_cell_symbol:
            self.__field[self.__end[0]][self.__end[1]] = self.__water_cell_symbol

    def __build_graph(self, field):
        def get_next_nodes_coordinates(cur_x, cur_y):
            def check_next_node_coordinates(x, y):
                return (0 <= x < self.__rows_number and 0 <= y < self.__cols_number
                        and (self.__field[x][y] is not self.__ground_cell_symbol))

            coordinates_differences = [-1, 0], [0, -1], [1, 0], [0, 1]
            return [(cur_x + dif_x, cur_y + dif_y) for dif_x, dif_y in coordinates_differences
                    if check_next_node_coordinates(cur_x + dif_x, cur_y + dif_y)]

        cells_graph = {}
        for x, row in enumerate(field):
            for y, cell in enumerate(row):
                if cell is not self.__ground_cell_symbol:
                    cells_graph[(x, y)] = cells_graph.get((x, y), []) + get_next_nodes_coordinates(x, y)
        return cells_graph

    def print_field(self):
        print()
        for x in range(0, self.__rows_number):
            for y in range(0, self.__cols_number):
                print(self.__field[x][y], end='')
            print()

    def __find_path(self, start, goal, cells_graph):
        queue = deque([start])
        visited_nodes = {start: None}

        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break

            next_nodes = cells_graph[cur_node]
            for next_node in next_nodes:
                if next_node not in visited_nodes:
                    queue.append(next_node)
                    visited_nodes[next_node] = cur_node
        return visited_nodes

    def __show_path(self, visited_nodes: dict[tuple, Any], goal_node):
        visited_node = goal_node
        self.__field[visited_node[0]][visited_node[1]] = self.__finish_cell_symbol
        while visited_node and visited_node in visited_nodes:
            visited_node = visited_nodes[visited_node]
            if visited_node:
                self.__field[visited_node[0]][visited_node[1]] = self.__visited_cell_symbol
                if visited_nodes[visited_node] is None:
                    self.__field[visited_node[0]][visited_node[1]] = self.__start_cell_symbol
        self.print_field()

    def find_and_show_path(self):
        print(f'\nSearching the way for moving from {self.__start} to {self.__end} in this field: ')
        self.print_field()

        cells_graph = self.__build_graph(self.__field)
        visited_nodes = self.__find_path(self.__start, self.__end, cells_graph)

        print(f'\nFound the way for moving from {self.__start} to {self.__end}: ')
        self.__show_path(visited_nodes, self.__end)
