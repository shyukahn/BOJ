def plus(l):
    return int(l[0])+int(l[1])

n = int(input())

for i in range(n):
    print("Case #{}: {}".format(i+1, plus(input().split())))