n = int(input())
n -= 1
ans = 1
i = 1
while n > 0:
    n -= 6*i
    i += 1
    ans += 1
print(ans)