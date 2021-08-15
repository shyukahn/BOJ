import math

def C(n,r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

def H(n,r):
    return C(n+r-1,r)

ans = 1
n = int(input())
if n%2 == 0:
    for i in range(1,n//2+1):
        ans += H(n//2+1-i, 2*i)*(2**(n//2-i))
    ans += 2**(n//2)-1
else:
    for i in range(1,n//2+1):
        ans += H(n//2+2-i,2*i-1)*(2**(n//2+1-i))
print(ans%10007)