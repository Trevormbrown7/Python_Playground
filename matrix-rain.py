import os
import random
import shutil
import time

def matrix_rain():

    columns, rows = shutil.get_terminal_size()

    drops = [random.randint(-rows, 0) for _ in range(columns)]

    chars = "ABCDEFG"

    GREEN = "\033[32m"
    BOLD_GREEN = "\033[1;32m"
    RESET = "\033[0m"
    CLEAR = "\033[H\033[J"
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"

    print(CLEAR + HIDE_CURSOR, end="")

    try:
        while True:
            current_columns, current_rows = shutil.get_terminal_size()
            if current_columns != columns or current_rows != rows:
                columns, rows = current_columns, current_rows
                drops = [random.randint(-rows, 0) for _ in range(columns)]

            frame = []
            for row in range(rows):
                line = ""
                for col in range(columns):
                    drop_pos = drops[col]

                    if drop_pos == row:
                        line += f"{BOLD_GREEN}{random.choice(chars)}{RESET}"
                        # Trailing character stream behind the lead
                    elif 0 <= row < drop_pos and (drop_pos - row) < random.randint(10, rows):
                        line += f"{GREEN}{random.choice(chars)}{RESET}"
                        # Empty space where no rain is falling
                    else:
                        line += " "

                frame.append(line)

                print("\033[H" +
                    "\n".join(frame), end="")

                for col in range(columns):
                    drops[col] += 1

                    if drops[col] >= rows or (drops[col] > 0 and random.random() < 0.03):
                        drops[col] = random.randint(-5, 0)

                time.sleep(0.01)

    except KeyboardInterrupt:
        print(SHOW_CURSOR + RESET + CLEAR)

if __name__ == "__main__":
    matrix_rain()
