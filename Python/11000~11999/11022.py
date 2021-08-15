def plus(l):
    return int(l[0])+int(l[1])

n = int(input())

for i in range(n):
    u = input().split()
    print("Case #{}: {} + {} = {}".format(i+1, u[0], u[1], plus(u)))