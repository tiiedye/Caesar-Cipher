# Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


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


encrypt(text, shift)
decrypt(text, shift)
