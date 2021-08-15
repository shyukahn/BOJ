def plus(l):
    return int(l[0]) + int(l[1])

while True:
    userInput = input().split()
    if plus(userInput) != 0:
        print(plus(userInput))
    else:
        break