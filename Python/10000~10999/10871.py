[n,x] = input().split()
userInput = input().split()
answer = []
for i in userInput:
    if int(i) < int(x):
        answer.append(i)
for i in answer:
    print(i, end = " ")