
# STILL TO ADD!!!
# Need to add in a check/flag, so that when the fill is generated it will only generate
# a max of 2 STROKES in a row... 

import os
import random
import time
import sys

# ----------------------------
# Constants / Settings
# ----------------------------
COUNT_16 = ["1", "e", "+", "a", "2", "e", "+", "a", "3", "e", "+", "a", "4", "e", "+", "a"]
STROKES = ["R", "L", "K", "-"]

# ----------------------------
# Helper functions
# ----------------------------
def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")
def welcome_page() -> None:
    print("### Welcome Page ###")
    time.sleep(1)
def check_measures() -> int:
    while True:
        user_input = input("How many Measures? [1 or 2]\n").strip()
        if user_input in ("1", "2"):
            return int(user_input)
        print("### Invalid Input ###")
def check_beats() -> int:
    while True:
        user_input = input("8th notes, or 16th notes? [8 or 16]\n").strip()
        if user_input in ("8", "16"):
            return int(user_input)
        print("### Invalid Input ###")
def check_again() -> bool:
    while True:
        user_input = input("Generate another? [y/n]\n").strip().lower()
        if user_input in ("y", "n"):
            return user_input == "y"
        print("### Invalid Input ###")
def create(measures: int, beats: int, strokes: list[str], count_16: list[str]) -> tuple[list[str], list[str], list[str]]:
    """
    Returns:
      fill_list: list of strokes with '|' separators
      count_list: list of count tokens with '|' separators
    beats is expected to be 8 or 16.
    """
    fill_list: list[str] = []
    count_list: list[str] = []
    accent_list: list[str] = []

    for _ in range(measures):
        for _ in range(beats):
            stroke = random.choice(strokes)
            fill_list.append(stroke)
            r_int = random.randint(0, 2)
            if stroke in ("L", "R") and r_int == 0:
                accent_list.append("<")
            else:
                accent_list.append(" ")

        fill_list.append("|")
        accent_list.append("|")

        # --- Count generation ---
        if beats == 16:
            for j in range(16):
                count_list.append(count_16[j])
        else:  # beats == 8
            # Use every other item: 0,2,4,...,14
            for idx in range(0, 16, 2):
                count_list.append(count_16[idx])
        count_list.append("|")

        # # --- Accent generation ---
        # for i in range(len(fill_list)):
        #     if fill_list[i] == "R":
        #         accent_list.append("<")
        #     else:
        #         accent_list.append(" ")
        # accent_list.append("|")


    return fill_list, count_list, accent_list

# ----------------------------
# Main program
# ----------------------------
def main() -> None:
    running = True

    while running:
        clear_screen()
        welcome_page()
        measures = check_measures()
        clear_screen()
        beats = check_beats()
        clear_screen()

        fill_list, count_list, accent_list = create(measures, beats, STROKES, COUNT_16)

        # Build printable strings

        final_fill = " ".join(fill_list)
        final_count = " ".join(count_list)
        final_accent = " ".join(accent_list)
        message_l0 = ("|  R A N D O M   R U D I M E N T  |".center(len(final_fill), "#"))
        message_l1 = (f"|  {measures} measure(s)  |".center(len(final_fill), "-"))
        message_l2 = (f"|  {beats}-note Subdivision  |".center(len(final_fill), "-"))

        print(f"#{message_l0}#")
        print(f"-{message_l1}-")
        print(f"-{message_l2}-\n")
        print(f"| {final_accent}")
        print(f"| {final_fill}")
        print(f"| {final_count}\n")

        running = check_again()

    clear_screen()
    sys.exit()

if __name__ == "__main__":
    main()