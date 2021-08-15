x = int(input())
y = int(input())
def quad(a, b):
    if a>0 and b>0:
        return 1
    elif a<0 and b>0:
        return 2
    elif a<0 and b<0:
        return 3
    else:
        return 4
print(quad(x, y))