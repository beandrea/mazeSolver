import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self) -> None:
        num_cols = 12
        num_rows = 10
        t_maze = Maze(0, 0, num_rows, num_cols, 10, 10, None)

        self.assertEqual(
            len(t_maze.getCells()), num_cols)

        self.assertEqual(
            len(t_maze.getCells()[0]), num_rows)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        t_maze = Maze(0, 0, num_rows, num_cols, 10, 10, None)

        self.assertEqual(
            t_maze.getCells()[0][0].has_top_wall, False)

        self.assertEqual(
            t_maze.getCells()[num_cols - 1][num_rows - 1].has_bottom_wall, False)

    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        t_maze = Maze(0, 0, num_rows, num_cols, 10, 10, None)

        for cell_list in t_maze.getCells():
            for cell in cell_list:
                self.assertEqual(cell.visited, False)

if __name__ == '__main__':
    unittest.main()
