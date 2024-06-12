import unittest.mock as mock
import unittest

from maze import Maze


@mock.patch("maze.Maze._draw_cell")
@mock.patch("maze.Maze._break_entrance_and_exit")
@mock.patch("maze.Maze._break_walls_r")
class MazeTests(unittest.TestCase):
    def test_maze_create_cells(self, *argv):
        rows = 10
        cols = 12

        maze = Maze(rows, cols)
        self.assertEqual(
            len(maze._cells[0]),
            rows
        )
        self.assertEqual(
            len(maze._cells),
            cols
        )

    def test_maze_create_cells_large(self, *argv):
        rows = 128
        cols = 192

        maze = Maze(rows, cols)
        self.assertEqual(
            len(maze._cells[0]),
            rows
        )
        self.assertEqual(
            len(maze._cells),
            cols
        )

    def test_maze_negative_arg(self, *argv):
        rows = -10
        cols = -12

        self.assertRaises(ValueError, Maze, rows, cols)

    def test_maze_wrong_arg_type(self, *argv):
        rows = "12"
        cols = True

        self.assertRaises(TypeError, Maze, rows, cols)


if __name__ == "__main__":
    unittest.main()
