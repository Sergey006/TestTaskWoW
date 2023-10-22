from second_task.models.shapes.base_shape import BaseShape


class Rectangle(BaseShape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def draw(self):
        print(f'Drawing Rectangle with height={self.height} and width={self.width}')
        for i in range(0, self.height):
            for x in range(0, self.width):
                print('*', end="")
            print()
