import random

from third_task.path_finder import PathFinder


class TestPathFinder:

    def test_run_path_finder(self):
        number_of_rows = random.randint(5, 50)
        number_of_cols = random.randint(5, 50)

        start_position = (random.randint(0, number_of_rows - 1), random.randint(0, number_of_cols - 1))
        end_position = (random.randint(0, number_of_rows - 1), random.randint(0, number_of_cols - 1))

        finder = PathFinder(number_of_rows, number_of_cols, start_position, end_position)
        finder.find_and_show_path()
