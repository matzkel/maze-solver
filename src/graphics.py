from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__running = False

        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self._close)

        if not isinstance(width, int):
            raise TypeError("width argument must be an integer")
        if width < 0:
            raise ValueError("width argument must be a greater than 0")
        
        if not isinstance(height, int):
            raise TypeError("height argument must be an integer")
        if height < 0:
            raise ValueError("height argument must be greater than 0")

        # Account for border width of lines
        self._width = width + 2
        self._height = height + 2

        self.__canvas = Canvas(
            self.__root,
            bg="white",
            width=self._width,
            height=self._height
        )

        self.__canvas.pack(fill=BOTH, expand=1)

    def draw_line(self, line, fill_color):
        if not isinstance(line, Line):
            raise TypeError("line argument must be a 'Line'")

        line._draw(self.__canvas, fill_color)

    def _redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self._redraw()

    def _close(self):
        self.__running = False


class Line():
    def __init__(self, point_a, point_b):
        if not isinstance(point_a, Point):
            raise TypeError("point_a argument must be a 'Point'")
        self.__point_a = point_a

        if not isinstance(point_b, Point):
            raise TypeError("point_b argument must be a 'Point'")
        self.__point_b = point_b

    def _draw(self, canvas, fill_color):
        canvas.create_line(
            self.__point_a.x,
            self.__point_a.y,
            self.__point_b.x,
            self.__point_b.y,
            fill=fill_color,
            width=2
        )


class Point():
    def __init__(self, x, y):
        self.x = x # x = 0 is the left of the screen
        self.y = y # y = 0 is the top of the screen
