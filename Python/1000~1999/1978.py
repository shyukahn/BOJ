import math

def isprime(n):
    result = 1
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            result = 0
            break
    if n == 1:
        result = 0
    return result
n = int(input())
ans = 0
userInput = list(map(int, input().split()))
for i in userInput:
    ans += isprime(i)
print(ans)