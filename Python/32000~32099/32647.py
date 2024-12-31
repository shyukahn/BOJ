import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

A, B, K = map(int, input().split())

primes = [i for i in range(A, min(B, K) + 1) if is_prime(i)]
num_count = {0: 1} # num_count[n] = number of ways to get n

for p in primes:
    new_num_count = {}
    
    # Add p to each number in num_count and get new numbers
    for k, v in num_count.items():
        if k + p <= K:
            new_num_count[k + p] = v + num_count.get(k + p, 0)
        
    # Update num_count
    num_count = num_count | new_num_count

print(num_count.get(K, 0))