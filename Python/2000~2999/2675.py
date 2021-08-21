import sys

input = sys.stdin.readline

for i in range(int(input())):
    r, s = input().split()
    r = int(r)
    for c in s:
        print(c * r, end="")
    print()
