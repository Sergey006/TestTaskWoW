from second_task.models.shapes.base_shape import BaseShape


class Triangle(BaseShape):

    def __init__(self, height):
        self.height = height
        self.base_width = height * 2 - 1

    def draw(self):
        if self.height > 0:
            print(f'Drawing Triangle with height={self.height}')
            for i in range(1, self.height * 2):
                print(' ' * (self.base_width - i), end="")
                print('*' * (i * 2 - 1), end="")
                print()
