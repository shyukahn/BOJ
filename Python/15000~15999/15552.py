import sys

def plus(l):
    return int(l[0])+int(l[1])

n = int(sys.stdin.readline())
for i in range(n):
    print(plus(sys.stdin.readline().split()))