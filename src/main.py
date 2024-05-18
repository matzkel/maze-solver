from graphics import Window, Line, Point


def main():
    window = Window(800, 600)
    window.draw_line(Line(Point(8, 8), Point(792, 8)), "red")
    window.wait_for_close()

if __name__ == "__main__":
    main()
