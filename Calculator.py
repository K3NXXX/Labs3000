x = "e"
while x == "e":
    num1 = int(input("Enter first number: "))
    num2 = input("Choose an operation:")
    num3 = int(input("Enter second number: "))

    if num2 == "+":
        print("Result : ", num1 + num3)
    elif num2 == "-":
        print("Result : ", num1 - num3)
    elif num2 == "*":
        print("Result : ", num1 * num3)
    elif num2 == "**":
        print("Result : ", num1 ** num3)
    elif num2 == "/" and num3 == 0:
        print("Бліч топ")
    elif num2 == "/":
        print("Result : ", num1 / num3)
    x = input("Press 'e' to continue ")








