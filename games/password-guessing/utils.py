def generate_feedback(secret, guess):
    """
    Returns a list of feedback symbols:
    ✅ correct position
    🔁 correct char wrong position
    ❌ not present
    """
    
    feedback = [""] * len(secret)
    secret_used = [False] * len(secret)
    guess_used = [False] * len(secret)

    # PASS 1: Exact matches
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            feedback[i] = "✅"
            secret_used[i] = True
            guess_used[i] = True

    # PASS 2: Misplaced matches
    for i in range(len(secret)):
        if i < len(guess) and not guess_used[i]:
            for j in range(len(secret)):
                if not secret_used[j] and guess[i] == secret[j]:
                    feedback[i] = "🔁"
                    secret_used[j] = True
                    guess_used[i] = True
                    break

    # PASS 3: Not present
    for i in range(len(secret)):
        if i >= len(guess) or not guess_used[i]:
            feedback[i] = "❌"

    return feedback

def format_feedback(guess, feedback):
    """
    Returns clean display string
    """
    result = []
    for i in range(len(feedback)):
        char = guess[i] if i < len(guess) else "_"
        result.append(f"{char}:{feedback[i]}")
    return "  ".join(result)