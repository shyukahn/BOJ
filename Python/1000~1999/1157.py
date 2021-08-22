nums = [0 for i in range(26)]
word = input().upper()

for i in range(26):
    nums[i] = word.count(chr(ord('A') + i))

maxNum = max(nums)
if nums.count(maxNum) > 1:
    print("?")
else:
    print(chr(ord('A') + nums.index(maxNum)))
