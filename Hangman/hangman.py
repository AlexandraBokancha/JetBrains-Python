import random

words = ["python", "java", "swift", "javascript"]
secret_word = random.choice(words)
result = ""
won = 0
lost = 0

print('H A N G M A N')


def game():
    letter_guessed = list("-" * len(secret_word))
    tries = 8
    used_letters = []

    while True:

        print()
        print(''.join(letter_guessed))
        guess = input("Input a letter: ")
        letters_used = []

        if len(guess) != 1:
            print('Please, input a single letter.')

        elif guess in used_letters and guess.islower() is True and guess.isalpha() is True:
            print("You've already guessed this letter.")

        elif guess.islower() is False or guess.isalpha() is False:
            print('Please, enter a lowercase letter from the English alphabet.')


        elif guess in secret_word:
            for i, x in enumerate(secret_word):
                if secret_word[i] == guess:
                    letter_guessed[i] = guess


        elif guess not in secret_word and len(guess) == 1 and guess.islower() is True:
            tries -= 1
            print("That letter doesn't appear in the word.")

        if tries == 0:
            print("You lost!")
            break


        elif "".join(letter_guessed) == secret_word:
            result = "win"
            break

        used_letters.append(guess)

    if tries > 0:
        print(f'You guessed the word {secret_word}!')
        print('You survived!')
        return result


def results(won, lost):
    return f'You won: {won} times \n'  f'You lost: {lost} times'


while True:

    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

    if menu == "play":
        result = game()
        if result == "win":
            won = won + 1
        else:
            lost = lost + 1
    elif menu == "results":
        print(results(won, lost))
    else:
        break



