from graphics import Window
from maze import Maze


def main():
    window = Window(800, 600)
    maze = Maze(10, 10, window)

    window.wait_for_close()


if __name__ == "__main__":
    main()
