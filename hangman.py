import random

def get_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("🎮 Welcome to Hangman!")
    print(f"You have {max_incorrect} incorrect guesses allowed.")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_incorrect:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            incorrect_guesses += 1
            print(f"❌ Incorrect! You have {max_incorrect - incorrect_guesses} guesses left.")

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You've guessed the word!")
            break
    else:
        print(f"💀 Game Over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
