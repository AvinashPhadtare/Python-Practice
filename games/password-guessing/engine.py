import random
import string


# Sample word list (you can expand this)
words = ["apple", "dog", "train", "cloud", "river", "ghost", "alpha"]

# Symbols list
symbols = ["@", "#", "$", "%", "&", "!"]


def generate_password(level):
    word = random.choice(words)
    number = str(random.randint(0,999))
    symbol = random.choice(symbols)

    if level == 'easy':
        password = word
    elif level == 'medium':
        password = f'{word}{number}'
    elif level == 'hard':
        password = f'{word}{symbol}{number}'
    else:
        print("Invalid Input(level)")
    
    return password



def get_valid_difficulty():
    level = input("Enter difficulty(easy / medium / hard): ").lower().strip()

    if level not in ["easy", "medium", "hard"]:
        print("⚠️ Invalid choice.")
        return

    return level
