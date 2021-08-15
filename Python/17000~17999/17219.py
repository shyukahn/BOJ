import sys

n, m = map(int, sys.stdin.readline().split())
passwords = {}
for i in range(n):
    a,b=sys.stdin.readline().split()
    passwords[a] = b
for i in range(m):
    sys.stdout.write(passwords[sys.stdin.readline().rstrip("\n")]+"\n")