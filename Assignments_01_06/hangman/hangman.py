import random

words = ["python", "hangman", "game", "program", "developer", "computer"]

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()  

    lives = 6 

    while len(word_letters) > 0 and lives > 0:
    
        print(f"\nYou have {lives} lives left. Used letters: {' '.join(used_letters)}")
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_display))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✅ Good guess!")
            else:
                lives -= 1
                print("❌ Wrong guess.")
        elif user_letter in used_letters:
            print("⚠️ You already guessed that letter.")
        else:
            print("⛔ Invalid input. Please enter a valid letter.")

    if lives == 0:
        print(f"\n💀 You died! The word was: {word}")
    else:
        print(f"\n🎉 Congratulations! You guessed the word: {word}!")

if __name__ == "__main__":
    hangman()
