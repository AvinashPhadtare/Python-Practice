from engine import generate_password,get_valid_difficulty
from utils import generate_feedback, format_feedback


def show_welcome():
    print("=================================")
    print("🔐 PASSWORD GUESSING GAME")
    print("=================================")
    print("Rules:")
    print("- Guess the hidden password")
    print("- Choose difficulty level")
    print("- Try until you win")
    print("=================================\n")


def start_game():
    count = int(0)
    # Step 1: Welcome + Rules
    show_welcome()

    # Step 2: Difficulty Input
    level = get_valid_difficulty()

    # Step 3: Select Secret Word
    secret = generate_password(level)

    # Step 4: Show length only (not the word)
    print(f"\n🔎 The password has {len(secret)} characters.\n")

    # TEMP (for testing, remove later)
    print(f"[DEBUG] Secret word: {secret}")

    # Step 5: Basic Guess Loop (Phase 1 simple version)
    while True:
        guess = input("Enter your guess: ").lower().strip()

        if not guess:
            print("⚠️ Empty input not allowed")
            continue
            
        

        if guess == secret.lower():

            print(f"\n🎉 Correct! You guessed the password in {count+1} attempts")
            break
        else:
            feedback = generate_feedback(secret.lower(), guess)
            display = format_feedback(guess, feedback)

            print(f'\n{display}')
            print("\n    ⚠️ Try again!   \n ")
            
        count += 1


if __name__ == "__main__":
    start_game()
