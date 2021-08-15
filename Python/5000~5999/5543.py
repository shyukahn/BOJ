price = []
for i in range(5):
    price.append(int(input()))
print(min(price[0],price[1],price[2])+min(price[3],price[4])-50)