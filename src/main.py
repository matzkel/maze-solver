from graphics import Window, Point
from cell import Cell


def main():
    window = Window(800, 600)
    
    cell_a = Cell(Point(40, 40), Point(160, 256), window)
    cell_a.draw()

    cell_b = Cell(Point(80, 80), Point(128, 368), window)
    cell_b.draw()

    cell_a.draw_move(cell_b)

    window.wait_for_close()

if __name__ == "__main__":
    main()
