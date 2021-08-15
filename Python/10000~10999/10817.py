num = list(map(int, input().split()))
num.remove(max(num))
num.remove(min(num))
print(num[0])