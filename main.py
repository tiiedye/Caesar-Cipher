# Caesar Cipher
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
alphabet_len = len(alphabet)


def encrypt(message, spaces):
    output = ""
    shift_int = int(spaces)

    if shift_int > alphabet_len:
        shift_int = shift_int % alphabet_len

    for i in message:
        if i in alphabet:
            index = alphabet.index(i)
            if index + shift_int > alphabet_len:
                new_shift = (index + shift_int) - alphabet_len
                output += alphabet[new_shift]
            else:
                output += alphabet[index + shift_int]
        else:
            output += i
    print(f"The encoded text is: {output}")


def decrypt(message, spaces):
    output = ""
    shift_int = int(spaces)

    if shift_int > alphabet_len:
        shift_int = shift_int % alphabet_len

    for i in message:
        if i in alphabet:
            index = alphabet.index(i)
            output += alphabet[index - shift_int]
        else:
            output += i
    print(f"The decoded text is: {output}")


print(art.logo)
direction = "start"

while direction != "q":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'Q' to quit:\n").lower()

    if direction == "encode":
        text = input("Type your message to encode:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your encoded message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    elif direction == "q":
        print("Goodbye!")
    else:
        print("Action undefined, please try again!")
