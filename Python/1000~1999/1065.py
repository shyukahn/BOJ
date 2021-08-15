def isHan(n: int):
    digits = []
    while n > 0:
        digits.append(n%10)
        n //= 10
    
    if len(digits) < 3:
        return True
    d = digits[1] - digits[0]
    for i in range(2, len(digits)):
        if digits[i] - digits[i-1] != d:
            return False
    return True

n = int(input())
cnt = 0
for i in range(1, n+1):
    if isHan(i):
        cnt += 1

print(cnt)
