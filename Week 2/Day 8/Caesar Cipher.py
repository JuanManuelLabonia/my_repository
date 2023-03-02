import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']


def caesar(text, shift, direction):
    cipher_text = ""
    for letter in text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift
                new_position %= 26
            elif direction == "decode":
                new_position = position - shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(f"The {direction}d text is: '{cipher_text}'")


end_game = False

while end_game == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    opinion = input(
        'Would you like to restart the program? Type "yes" or "no" ').lower()
    if opinion == "no":
        print("Goodbye")
        end_game = True
    else:
        end_game = False
