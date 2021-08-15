N = int(input())
a = N//5
if N != 4 and N != 7:
    while (N-2*a)%3 != 0:
        a -= 1
    print((N-2*a)//3)
else:
    print(-1)