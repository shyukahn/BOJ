def cycle(num):
    return 10*(num%10)+(num//10+num%10)%10

n = int(input())
length = 1
n1 = n

while True:
    n = cycle(n)
    if n1 == n:
        break
    else:
        length += 1
print(length)