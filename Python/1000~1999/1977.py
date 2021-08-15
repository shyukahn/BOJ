import math
sqr = []
for i in range(100):
    sqr.append((i+1)**2)
m = int(input())
n = int(input())
mr = int(math.sqrt(m))
nr = int(math.sqrt(n))
s = 0
if mr == nr:
    if math.sqrt(m) == mr:
        print(m)
        print(m)
    else:
        print(-1)
else:
    if math.sqrt(m) == mr:
        for i in range(mr-1,nr):
            s += sqr[i]
        print(s)
        print(m)
    else:
        for i in range(mr,nr):
            s += sqr[i]
        print(s)
        print(sqr[mr])
