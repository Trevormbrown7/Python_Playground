import random, os, time

# Variables
running = True
list_of_words = ["Python", "Kitchen", "Snake", "Dog", "Cat", "Table", "ShutYoBitchAssUp"]
word_to_guess = random.choice(list_of_words)
display = []
heart = "❤️ "
guessed_letters = []
guess = False
health = 0
number_of_guesses = 0
hangman_display = [
r"""
	 ___________
	|-/	   
	|/	   
	|	   
	|	  
	|	   
	|     
________|__________________
""",
r"""
	 ___________
	|-/	   |
	|/	   |
	|	   O
	|	  
	|	   
	|     
________|__________________
""",
r"""
	 ___________
	|-/	   |
	|/	   |
	|	   O
	|	   |
	|	   
	|     
________|__________________
""",
r"""
	 ___________
	|-/	   |
	|/	   |
	|	   O
	|	  /|
	|	   
	|     
________|__________________
""",
r"""
	 ___________
	|-/	   |
	|/	   |
	|	   O
	|	  /|\
	|	   
	|     
________|__________________
""",
r"""
	 ___________
	|-/	   |
	|/	   |
	|	   O
	|	  /|\
	|	   |
	|     
________|__________________
""",
r"""
	 ___________
	|-/	   |
	|/	   |
	|	   O
	|	  /|\
	|	   |
	|         /
________|__________________
""",
r"""
	 ___________
	|-/	   |
	|/	   |
	|	   X
	|	  /|\
	|	   |
	|         / \
________|__________________
""",
]

# Create the display
for l in word_to_guess:
    if l != " ":
        display.append("_")
    else:
        display.append(" ")

# Functions
def start_screen():
    global running
    running = True
    clear_screen()
    print("#"*25)
    print("/  Welcome to Hangman!  \\")
    print("#"*25)
    draw_hangman()
    time.sleep(1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def strikethrough(text):
    return ', '.join(c + '\u0336' for c in text)

def user_guess():
    global guess
    global health
    global running
    for letter in range(len(word_to_guess)):
        if user_input == word_to_guess[letter].lower():
            display[letter] = word_to_guess[letter]
            guess = True
    if not guess:
        print("Incorrect!")
        guessed_letters.append(user_input)
        health += 1
    else:
        print("Correct!")
        guess = False
    time.sleep(0.2)
    clear_screen()

def draw_hangman():
    global health
    print(hangman_display[health])
    health_left = len(hangman_display) - health
    print("Health left: " + heart * (health_left-1))
    print("Guessed letters: " + strikethrough(guessed_letters))

def check_health():
    global health
    global running
    global number_of_guesses
    if health == 7:
        print("Game over...")
        user = input("\nDo you want to play again?\n(y/n)\n").lower()
        if user == "y":
            start_screen()
        elif user == "n":
            running = False

def check_win():
    global display
    global running
    global health
    joined_list = "".join(display)
    if joined_list == word_to_guess:
        print("\nYou win!\n"
              f"Congratulations it took you {number_of_guesses} guesses.\n\nGoodbye.")
        running = False

start_screen()
while running:
    number_of_guesses += 1
    print("Guess a letter...")
    user_input = input(str(" ".join(display)) + "\n\n").lower()
    user_guess()
    draw_hangman()
    check_health()
    check_win()



