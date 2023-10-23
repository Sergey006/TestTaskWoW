import random

from third_task.path_finder import PathFinder


class TestPathFinder:

    def test_run_path_finder(self):
        m = random.randint(5, 50)
        n = random.randint(5, 50)

        a = (random.randint(0, m - 1), random.randint(0, n - 1))
        b = (random.randint(0, m - 1), random.randint(0, n - 1))

        finder = PathFinder(rows_qty=m, cols_qty=n, start_xy=a, end_xy=b)
        finder.find_and_show_path()
