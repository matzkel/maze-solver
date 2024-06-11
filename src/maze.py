from time import sleep
import random

from graphics import Window, Point
from cell import Cell


class Maze():
    def __init__(self, rows, cols, seed=None, window=None):
        self._cells = []

        if not isinstance(rows, int):
            raise TypeError("rows argument must be an integer")
        if rows < 0:
            raise ValueError("rows argument must be greater than 0")

        if not isinstance(cols, int):
            raise TypeError("cols argument must be an integer")
        if cols < 0:
            raise ValueError("cols argument must be greater than 0")

        self.__rows = rows
        self.__cols = cols

        if seed:
            self.__seed = random.seed(seed)

        self.__window = window
        if isinstance(self.__window, Window):
            self.__width = self.__window._width
            self.__height = self.__window._height

            self.__cell_size_x = (self.__width - 2) / self.__cols
            self.__cell_size_y = (self.__height - 2) / self.__rows
        
        self._create_cells()

    def _create_cells(self):
        for col in range(self.__cols):
            self._cells.append([
                Cell() for _ in range(self.__rows)
            ])
        
        for col in range(self.__cols):
            for row in range(self.__rows):
                self._draw_cell(col, row)

        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _draw_cell(self, i, j):
        if not isinstance(self.__window, Window):
            raise TypeError("window argument must be a 'Window'")

        cell = Cell(
            # 2, because we need to account for border width of lines
            Point(
                2 + self.__cell_size_x * i,
                self.__height - self.__cell_size_y * j
            ),
            Point(
                2 + self.__cell_size_x * (i + 1),
                self.__height - self.__cell_size_y * (j + 1)
            ), self.__window
        )

        cell.walls = self._cells[i][j].walls
        cell.visited = self._cells[i][j].visited

        self._cells[i][j] = cell

        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if not isinstance(self.__window, Window):
            raise TypeError("window argument must be a 'Window'")

        self.__window._redraw()
        sleep(0.02)

    def _break_entrance_and_exit(self):
        walls = self._cells[0][0].walls
        walls[2] = False
        self._draw_cell(0, 0)

        walls = self._cells[self.__cols - 1][self.__rows - 1].walls
        walls[3] = False
        self._draw_cell(self.__cols - 1, self.__rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            adj_cells = []

            # Left cell
            if i - 1 >= 0 and self._cells[i - 1][j].visited is False:
                adj_cells.append((i - 1, j, 0, 1))
            # Right cell
            if i + 1 < self.__cols and self._cells[i + 1][j].visited is False:
                adj_cells.append((i + 1, j, 1, 0))
            # Top cell
            if j + 1 < self.__rows and self._cells[i][j + 1].visited is False:
                adj_cells.append((i, j + 1, 3, 2))
            # Bottom cell
            if j - 1 >= 0 and self._cells[i][j - 1].visited is False:
                adj_cells.append((i, j - 1, 2, 3))
            
            if not adj_cells:
                self._draw_cell(i, j)
                return

            next_cell = adj_cells[random.randrange(len(adj_cells))]

            self._cells[i][j].walls[next_cell[2]] = False
            self._cells[next_cell[0]][next_cell[1]].walls[next_cell[3]] = False

            self._break_walls_r(next_cell[0], next_cell[1])
