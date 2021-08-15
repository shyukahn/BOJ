def plus(l):
    return int(l[0]) + int(l[1])

while True:
    try:
        userInput = input().split()
        print(plus(userInput))
    except:
        break