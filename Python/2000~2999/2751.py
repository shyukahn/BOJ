import sys
num = []
n = int(sys.stdin.readline())
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
for i in range(n):
    print(num[i])