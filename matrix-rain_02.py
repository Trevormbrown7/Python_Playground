import os
import random
import shutil
import time


def terminal_animate():

    char = ""
    grid = []

    GREEN = "\033[32m"
    BOLD_GREEN = "\033[1;32m"
    RESET = "\033[0m"
    CLEAR = "\033[H\033[J"
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"

    print(CLEAR + HIDE_CURSOR, end="")

    try:
        columns, rows = shutil.get_terminal_size()
        for x in range(rows):
            char = ""
            for y in range(columns):
                if y == 0:
                    char += f"{BOLD_GREEN}O"
                elif y == columns - 1:
                    char += f"{BOLD_GREEN}O"
                else:
                    char += f"{GREEN}x"

            grid.append(char)


        for i in range(len(grid)):
            print(grid[i])

    except KeyboardInterrupt:
        print(SHOW_CURSOR + RESET + CLEAR)

if __name__ == "__main__":
    terminal_animate()
