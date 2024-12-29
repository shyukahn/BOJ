import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split()) 
is_prime = [True for _ in range(N + 1)]

# Set false for non-prime numbers
for i in range(2, int(N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i ** 2, N + 1, i):
            is_prime[j] = False

# count[n] = number of prime numbers from 1 to n
count = [0 for _ in range(N + 1)]
cur_count = 0

for i in range(1, N + 1):
    if is_prime[i]:
        cur_count += 1
    count[i] = cur_count

for _ in range(M):
    a, b = map(int, input().split())
    print(str(count[b] - count[a - 1]) + '\n')