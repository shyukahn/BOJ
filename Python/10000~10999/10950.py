n = int(input())
l = []
for i in range(n):
    l = l + input().split()
for i in range(n):
    print(int(l[2*i])+int(l[(2*i)+1]))
