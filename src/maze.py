from time import sleep

from graphics import Window, Point
from cell import Cell


class Maze():
    def __init__(self, rows, cols, window=None):
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
        self._cells[i][j] = cell

        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if not isinstance(self.__window, Window):
            raise TypeError("window argument must be a 'Window'")

        self.__window._redraw()
        sleep(0.02)
