def f(x):
    if x%2==0:
        return " "
    else:
        return "*"

n = int(input())
if n==1:
    print("*")
else:
    for line in range(n):
        for i in range(n):
            print(f(i+1), end = "")
        print()
        for i in range(n):
            print(f(i), end = "")
        print()