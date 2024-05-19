from time import sleep

from graphics import Window, Point
from cell import Cell


class Maze():
    def __init__(self, rows, cols, window):
        self._cells = []
        self.__rows = rows
        self.__cols = cols

        self.__window = window
        self.__width = self.__window._width
        self.__height = self.__window._height

        self.__cell_size_x = (self.__width - 2) / self.__cols
        self.__cell_size_y = (self.__height - 2) / self.__rows
        
        self._create_cells()

    def _create_cells(self):
        for col in range(self.__cols):
            self._cells.append([
                Cell(
                    Point(0, 0),
                    Point(0, 0),
                    self.__window
                ) for _ in range(self.__rows)
            ])
        
        for col in range(self.__cols):
            for row in range(self.__rows):
                self._draw_cell(col, row)

    def _draw_cell(self, i, j):
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
        self.__window._redraw()
        sleep(0.02)
