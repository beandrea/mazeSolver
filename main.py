from graphics import Window
from maze import Maze
import random

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    size_of = random.randint()
    seed = 0

    for i in range(size_of):
        seed += ((10 ** i) * random.randint())

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)

    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()

if __name__ == "__main__":
    main()
