from graphics import Window, Line, Point


class Cell():
    def __init__(self, point_a=None, point_b=None, window=None):
        # Left, Right, Top, Bottom 
        self.walls = [True, True, True, True]
        self.visited = False
        
        # Top-left corner
        self.__point_a = point_a
        # Bottom-right corner
        self.__point_b = point_b

        self.__window = window
    
    def draw_move(self, to_cell, undo=False):
        if not isinstance(self.__point_a, Point):
            raise TypeError("point_a argument must be a 'Point'")
        if not isinstance(self.__point_b, Point):
            raise TypeError("point_b argument must be a 'Point'")
        
        if not isinstance(self.__window, Window):
            raise TypeError("window argument must be a 'Window'")

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
        if not isinstance(self.__point_a, Point):
            raise TypeError("point_a argument must be a 'Point'")
        if not isinstance(self.__point_b, Point):
            raise TypeError("point_b argument must be a 'Point'")

        if not isinstance(self.__window, Window):
            raise TypeError("window argument must be a 'Window'")
        
        if not isinstance(self.walls, list):
            raise TypeError("walls argument must be a list of booleans")

        for wall in self.walls:
            if not isinstance(wall, bool):
                raise TypeError("list indices must be booleans")
        
        # Left wall
        if self.walls[0]:
            line = Line(
                self.__point_a,
                Point(self.__point_a.x, self.__point_b.y)
            )
            self.__window.draw_line(line, "black")
        else:
            line = Line(
                self.__point_a,
                Point(self.__point_a.x, self.__point_b.y)
            )
            self.__window.draw_line(line, "white")
        # Right wall
        if self.walls[1]:
            line = Line(
                Point(self.__point_b.x, self.__point_a.y),
                self.__point_b
            )
            self.__window.draw_line(line, "black")
        else:
            line = Line(
                Point(self.__point_b.x, self.__point_a.y),
                self.__point_b
            )
            self.__window.draw_line(line, "white")
        # Top wall
        if self.walls[2]:
            line = Line(
                self.__point_a,
                Point(self.__point_b.x, self.__point_a.y)
            )
            self.__window.draw_line(line, "black")
        else:
            line = Line(
                self.__point_a,
                Point(self.__point_b.x, self.__point_a.y)
            )
            self.__window.draw_line(line, "white")
        # Bottom wall
        if self.walls[3]:
            line = Line(
                Point(self.__point_a.x, self.__point_b.y),
                self.__point_b
            )
            self.__window.draw_line(line, "black")
        else:
            line = Line(
                Point(self.__point_a.x, self.__point_b.y),
                self.__point_b
            )
            self.__window.draw_line(line, "white")
