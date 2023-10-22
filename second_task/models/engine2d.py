from typing import List

from second_task.models.colors import Colors
from second_task.models.shapes.base_shape import BaseShape


class Engine2D:
    color: Colors = None

    def __init__(self):
        self.canvas: List[BaseShape] = list()

    def draw(self):
        for shape in self.canvas:
            if self.color is not None:
                print(f'Current color is {self.color.name}. ', end='')
            shape.draw()
        self.canvas.clear()

    def add_shape(self, shape):
        self.canvas.append(shape)

    def set_color(self, color):
        self.color = color
        print(self.color.value, end='')
