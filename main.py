# Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(message, spaces):
    alphabet_len = len(alphabet)
    output = ""
    for i in message:
        index = alphabet.index(i)
        if index + int(spaces) > alphabet_len:
            new_shift = (index + int(spaces)) - alphabet_len
            output += alphabet[new_shift]
        else:
            output += alphabet[index + int(spaces)]
    print(f"The encoded text is: {output}")


def decrypt(message, spaces):
    output = ""
    for i in message:
        index = alphabet.index(i)
        output += alphabet[index - int(spaces)]
    print(f"The decoded text is: {output}")


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
    else:
        print("Action undefined, please try again!")
