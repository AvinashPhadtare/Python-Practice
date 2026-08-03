# input_handler.py

from config import MAX_LINES, MAX_BET, MIN_BET

def deposit():
    while True:
        amount = input("Enter deposit amount ₹")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Invalid input.")


def get_number_of_lines():
    while True:
        lines = input(f"Enter lines (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
        print("Invalid number of lines.")


def get_bet():
    while True:
        bet = input(f"Enter bet (₹{MIN_BET}-{MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
        print("Invalid bet amount.")