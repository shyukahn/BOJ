pibolist = [1, 1]
for i in range(2,45):
    pibolist.append(pibolist[i-2]+pibolist[i-1])
print(pibolist[int(input())-1])