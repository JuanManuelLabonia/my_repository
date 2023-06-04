import random
import hangman_art
import hangman_words
import platform
import os
# lets make a list of the words to check and the valid inputs
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
word_len = len(chosen_word)
print(chosen_word)
display = []

for letter in chosen_word:
    display += "_"

prettier_display1 = str()
a = 0
for space in display:
    prettier_display1 += display[a] + " "
    a += 1

print(prettier_display1)

lives = 6
print(f"You have {lives} lives")

end_game = False

while not end_game:
    if "_" not in display:
        limpiar_pantalla()
        print(hangman_art.stages[lives])
        print(f"You win with {lives} lives remaining.")
        end_game = True
    elif "_" in display:
        guess = input("Guess a letter: ").lower()
        limpiar_pantalla()
        if guess in display:
            print(f"You've already entered {guess}")
            print(hangman_art.stages[lives])
        for position in range(word_len):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print(hangman_art.stages[lives])
        if guess not in chosen_word:
            if lives > 0:
                print(hangman_art.stages[lives])
                lives -= 1
                print(
                    f"The letter {guess} is not in the word. You have {lives} lives left")
            elif lives == 0:
                print(hangman_art.stages[lives])
                print(f"The word was {chosen_word}. You lose.")
                end_game = True

    prettier_display = str()
    a = 0
    for space in display:
        prettier_display += display[a] + " "
        a += 1
    print(prettier_display)
