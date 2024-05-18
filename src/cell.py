from graphics import Line, Point


class Cell():
    def __init__(self, point_a, point_b, window):
        # Left, Right, Top, Bottom 
        self.walls = [True, True, True, True]
        
        # Top-left corner
        self.__point_a = point_a
        # Bottom-right corner
        self.__point_b = point_b

        self.__window = window
    
    def draw_move(self, to_cell, undo=False):
        fill_color = "gray" if undo else "red"

        # The center of the cell is the midpoint
        # of the diagonal end of the cell
        # ( (x1 + x2) / 2, (y1 + y2) / 2 )
        from_coords = Point(
            (self.__point_a.x + self.__point_b.x) / 2,
            (self.__point_a.x + self.__point_b.y) / 2
        )

        to_coords = Point(
            (to_cell.__point_a.x + to_cell.__point_b.x) / 2,
            (to_cell.__point_a.x + to_cell.__point_b.y) / 2
        )

        line = Line(from_coords, to_coords)
        self.__window.draw_line(line, fill_color)

    def draw(self):
        # Left wall
        if self.walls[0]:
            line = Line(
                self.__point_a,
                Point(self.__point_a.x, self.__point_b.y)
            )
            self.__window.draw_line(line, "black")
        # Right wall
        if self.walls[1]:
            line = Line(
                Point(self.__point_b.x, self.__point_a.y),
                self.__point_b
            )
            self.__window.draw_line(line, "black")
        # Top wall
        if self.walls[2]:
            line = Line(
                self.__point_a,
                Point(self.__point_b.x, self.__point_a.y)
            )
            self.__window.draw_line(line, "black")
        # Bottom wall
        if self.walls[3]:
            line = Line(
                Point(self.__point_a.x, self.__point_b.y),
                self.__point_b
            )
            self.__window.draw_line(line, "black")
