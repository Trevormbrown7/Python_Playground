import random, os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

width = 40
def welcome_message(text=""):
    print(f"|{text.center(width - 2)}|")

def welcome():
    clear_screen()
    print("o0" + "O" * (width - 4) + "0o")
    welcome_message(".   `   ,  `   *     .     ,  *   .")
    welcome_message("Welcome To The Number Guesser!")
    welcome_message("  *   `  ,    *  '   `    .    *    `")
    print("|" + "_" * (width - 2) + "|")
    print()
    print("Press [ENTER] to play".center(width, " "))
    input()
    clear_screen()

def check_guess(user_input, r_number, health):
    if user_input == "help":
        clear_screen()
        print(f"The random number is {r_number}")
        time.sleep(1)
        return False, health

    try:
        guess = int(user_input)
    except ValueError:
        print("Please enter a number.")
        return False, health

    if guess == r_number:
        print("Congratulations, you won!")
        time.sleep(1)
        return True, health
    else:
        if guess > r_number:
            print("Incorrect...\nToo high!")
        elif guess < r_number:
            print("Incorrect...\nToo low!")
        health -= 1
        time.sleep(0.8)
        return False, health

def play_again():
    clear_screen()
    user = input("Do you want to play again? (y/n)\n").lower()
    while user != "y" and user != "n":
        clear_screen()
        print("## Invalid input. ##")
        user = input("Do you want to play again? (y/n)\n").lower()

    if user == "y":
        clear_screen()
        return True
    else:
        clear_screen()
        print("Goodbye!")
        return False

def main():
    health = 5
    r_number = random.randint(1, 10)
    while health > 0:
        health_display = "❤️ " * health
        print(f"Health: {health_display}".ljust(30, " "))
        user_input = input("Guess a number (1-10)...\n").lower()
        win, health = check_guess(user_input, r_number, health)
        time.sleep(0.4)
        clear_screen()
        if win:
            break

    if health == 0:
        clear_screen()
        print("Out of lives...\nGAME OVER")
        time.sleep(1.5)

welcome()
while True:
    main()
    if not play_again():
        break

# Just cleaned some things up