x = "f"
while x == "f":
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ12345678901234567890'
    k = 2
    text = input("Enter a text to encrypt: ").upper()
    result = ""
    for letter in text:
        place = alphabet.find(letter)
        newplace = place + k
        if letter in alphabet:
            result = result + alphabet[newplace]
        else:
            result = result + letter
    print("Your encrypted text: ", result)

    x = input("Enter 'f' to continue of another button to exit: ")

