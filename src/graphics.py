from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__running = False

        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False


class Line():
    def __init__(self, point_a, point_b):
        self.__point_a = point_a
        self.__point_b = point_b

    def draw(self, canvas, fill_color):
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

