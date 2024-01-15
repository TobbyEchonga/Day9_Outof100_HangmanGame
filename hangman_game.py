import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "developer", "software"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        print("\nAttempts left:", attempts_left)
        print("Current word:", display_word(word_to_guess, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            print("Incorrect guess!")
            attempts_left -= 1
        else:
            print("Good guess!")

        if set(word_to_guess) <= guessed_letters:
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

    else:
        print("\nSorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
