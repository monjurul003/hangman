import random
import string
from words import words


def get_valid_words() -> string:
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman() -> None:
    word = get_valid_words()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print('So far you have used the following characters: ', ' '.join(used_letters))

        word_status = [letter if letter in used_letters else '-' for letter in word]
        print('You have ',lives, 'lives left and current status of the word: ', ' '.join(word_status))

        user_input = input('Insert your guess: ').upper()
        if user_input not in alphabet:
            print('Invalid input. Please try again.')
        else:
            if user_input not in used_letters:
                used_letters.add(user_input)
                if user_input in word_letters:
                    word_letters.remove(user_input)
                else:
                    print('Wrong guess. try again')
                    lives -= 1
            else:
                print('You have already used that character.')
    if lives == 0:
        print('You lose! Actual word was: ', word)
    else:
        print('You win! Actual word was: ', word)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hangman()

