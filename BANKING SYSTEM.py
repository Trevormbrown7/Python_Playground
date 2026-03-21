import sys
import time
import os
import string
from unicodedata import name

class Account:
    def __init__(self, name, age, balance, password):
        self.name = name
        self.age = age
        self.balance = balance
        self.password = password

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Balance: ${self.balance}"

    def check_login(self, entered_password):
        return entered_password == self.password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def transfer(self, recipient, amount):
        if amount > self.balance:
            print("Insufficient funds for transfer.")
        elif amount <= 0:
            print("Transfer amount must be positive.")
        else:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred ${amount} to {recipient.name}. \nYour new balance: ${self.balance}")
    
    def welcome_message(self):
        print("-~=\_____________              _____________/=~-".center(50, "-"))
        print("=~-~=~-~=~-                         -~=~-~=~-~=".center(50, "-"))
        print(f"=~-~=~-     Welcome, {self.name}!     -~=~-~=".center(50, "-"))
        print("=~-   What would you like to do today?   -~=".center(50, "-"))
        print("=~-                                          -~=".center(50, "-"))
        print(">>>   1. DEPOSIT   <<<".center(50, " "))
        print(">>>   2. WITHDRAW   <<<".center(50, " "))
        print(">>>   3. BALANCE   <<<".center(50, " "))
        print(">>>   4. TRANSFER   <<<".center(50, " "))
        print(">>>   5. LOGOUT   <<<".center(50, " "))
        print("-----/|                           |\-----".center(50, "-"))
        print("     ~>>>       [ Q ] TO QUIT       <<<~     ".center(50, "-"))
        print("\n")

    def welcome(self):
        self.welcome_message()
        menu_choice = input("-->>  ")
        if menu_choice == "1": # DEPOSIT
            clear()
            amount = float(input("Enter amount to deposit: $"))
            self.deposit(amount)
            time.sleep(1)
            input("\nPress Enter to return to the menu...")
            clear()
            self.welcome()
        elif menu_choice == "2": # WITHDRAW
            clear()
            amount = float(input("Enter amount to withdraw: $"))
            self.withdraw(amount)
            time.sleep(1)
            input("\nPress Enter to return to the menu...")
            clear()
            self.welcome()
        elif menu_choice == "3": # BALANCE
            clear()
            print(" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \n"
                f"  \ \ \ \ Your current balance is: ${self.balance}"
                "\n   \ \ \ \ \ \ \ \ \ \ \ \ \ ")
            time.sleep(1)
            input("\nPress Enter to return to the menu...")
            clear()
            self.welcome()
        elif menu_choice == "4": # TRANSFER
            clear()
            recipient_name = input("Enter recipient's name: ")
            recipient = None
            for acct in accounts:
                if acct.name == recipient_name:
                    recipient = acct
                    break
            if not recipient:
                print("Recipient not found.")
                time.sleep(1)
                input("\nPress Enter to return to the menu...")
                clear()
                self.welcome()
            else:
                amount = float(input("Enter amount to transfer: $"))
                self.transfer(recipient, amount)
                time.sleep(1)
                input("\nPress Enter to return to the menu...")
                clear()
                self.welcome()
        elif menu_choice == "5": # LOGOUT
            clear()
            print("Logging out...")
            time.sleep(1)
            clear()
            start_message(today_date)
        elif menu_choice.lower() == "q": # QUIT
            print("Thank you for banking with us! Goodbye!")
            time.sleep(1)
            sys.exit()

p1 = Account("Trevor", 28, 100000, 1234)
p2 = Account("Brie", 25, 500000, 4321)
p3 = Account("Scout", 40, 750000, 1111)
p4 = Account("Star", 2, 12000, 2222)

accounts = [p1, p2, p3, p4]

today_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def start_message(date):
    print("" \
    "\n|=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=|\n" \
    "    Welcome to Brownie's Bank! \n" \
    f"       {date}\n" \
    "|=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=| \n")

def clear():
    print("\033[H\033[J", end="")
    #os.system("cls" if os.name == "nt" else "clear")

clear()
start_message(today_date)

time.sleep(1)
while True:
    name = input("Enter your name: ")
    entered_password = int(input("Enter your password: "))

    logged_in = None
    for acct in accounts:
        if acct.check_login(entered_password):
            logged_in = acct
            clear()
            break
   
    if logged_in:
        logged_in.welcome()
        running = False
    else:
        print("Login failed. Please try again.")

sys.exit()