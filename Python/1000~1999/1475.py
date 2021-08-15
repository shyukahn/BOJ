n = input()
num = []
ans = []
for i in range(10):
    num.append(n.count("{}".format(i)))
for i in [0,1,2,3,4,5,7,8]:
    ans.append(num[i])
ans.append((num[6]+num[9]+1)//2)
print(max(ans))