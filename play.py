play = True

while play:

    x = input("Enter a number: ")
    y = input("Enter a number: ")

    x = int(x)
    y = int(y)

    print(type(x))
    print(type(y))

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)

    if input("Play again? ") == "no":
        play = False