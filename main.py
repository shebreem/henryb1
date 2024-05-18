import random
import time

def generateSequence(length, dif):
    sequence = []
    start = random.randint(5, 100)
    previous = start
    for i in range(length):
        if i == 0:
            sequence.append(previous)
        else:
            previous += dif
            sequence.append(previous)
    return sequence

def shiftchar(char, shift):
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    ]
    reverse = {v: k for k, v in enumerate(alphabet)}  # Corrected index
    if char.lower() in alphabet:
        char = char.lower()
        shifted_index = (alphabet.index(char) + shift) % 26
        shift_char = alphabet[shifted_index]
        return shift_char
    else:
        return char

banner = """
██╗  ██╗███████╗███╗   ██╗██████╗ ██╗   ██╗
██║  ██║██╔════╝████╗  ██║██╔══██╗╚██╗ ██╔╝
███████║█████╗  ██╔██╗ ██║██████╔╝ ╚████╔╝ 
██╔══██║██╔══╝  ██║╚██╗██║██╔══██╗  ╚██╔╝  
██║  ██║███████╗██║ ╚████║██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   
"""
tabbing = "       -->"

print(f"\033[1;36m{banner}\033[0m")
choice = input(f"\033[1;36mChoose an option (encrypt/decrypt): \033[0m").lower()

if choice == "encrypt":
    message = input(f"\033[1;36mMessage: \033[0m")
    length = len(message)
    dif = random.randint(1, 20)
    sequence = generateSequence(length, dif)

    encrypted_message = ""
    for i, char in enumerate(message):
        encrypted_message += shiftchar(char, sequence[i])

    print(f"{tabbing}\033[1;36mdif: {dif}, sequence: {sequence}\033[0m")
    print(f"{tabbing}\033[1;36mEncrypted message: {encrypted_message}\033[0m")

elif choice == "decrypt":
    sequence_input = input(f"\033[1;36mSequence (comma-separated numbers): \033[0m")
    sequence = [int(num) for num in sequence_input.split(',')]
    encrypted_message = input(f"\033[1;36mEncrypted message: \033[0m")

    decrypted_message = ""
    for i, char in enumerate(encrypted_message):
        decrypted_message += shiftchar(char, -sequence[i])

    print(f"{tabbing}\033[1;36mDecrypted message: {decrypted_message}\033[0m")

else:
    print(f"{tabbing}\033[1;31mInvalid option. Please choose either 'encrypt' or 'decrypt'.\033[0m")

time.sleep(15)
