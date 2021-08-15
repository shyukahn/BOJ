n = int(input())
i = 1
temp = n
while temp > 0:
    temp -= i
    i += 1
if i % 2 == 0:
    up = i*(i-1)//2 - n + 1
    down = i - up
else:
    down = i*(i-1)//2 - n + 1
    up = i - down

print("{}/{}".format(up, down))