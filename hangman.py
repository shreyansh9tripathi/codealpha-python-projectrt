import random
words = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "time")
print("Welcome to Hangman!\n")
hangman_art={
    0: "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    1: "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    2: "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    3: "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    4: "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    5: "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    6: "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
}
def display_hangman(wrong_guesses):
    for line in hangman_art[wrong_guesses].splitlines():
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = "'_'" * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        display_answer(answer)
        guess = input("enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            hint = ''.join([letter if letter in guessed_letters else '_' for letter in answer])
            if '_' not in hint:
                print(f"Congratulations! You've guessed the word: {answer}")
                is_running = False
        else:
            wrong_guesses += 1
            if wrong_guesses >= 6:
                display_hangman(wrong_guesses)
                print(f"Game over! The correct word was: {answer}")
                is_running = False


if __name__ == "__main__":
    main()          

