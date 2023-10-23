import math

from second_task.models.shapes.base_shape import BaseShape


class Circle(BaseShape):

    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        if self.radius > 0:
            print(f'Drawing Circle with radius={self.radius}')
            for y in range(-self.radius, self.radius + 1):
                for x in range(-self.radius, self.radius + 1):
                    distance = math.sqrt(x ** 2 + y ** 2)
                    if distance <= self.radius:
                        print('*', end="")
                    else:
                        print(' ', end="")
                print()
