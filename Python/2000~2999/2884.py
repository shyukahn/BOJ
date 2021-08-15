timeinput = input().split()
(hour1, minute1) = (int(timeinput[0]), int(timeinput[1]))

if minute1 >= 45:
    minute = minute1 - 45
    dif = 0
else:
    minute = minute1 + 15
    dif = 1
hour = hour1 - dif
if hour == -1:
    hour = 23

print("{} {}".format(hour, minute))