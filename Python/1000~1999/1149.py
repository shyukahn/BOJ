n = int(input())
cost = []
dp = []
for i in range(n):
    cost.append(list(map(int, input().split())))
dp.append(cost[0])
for i in range(1,n):
    dp.append([cost[i][0]+min(dp[i-1][1],dp[i-1][2]),cost[i][1]+min(dp[i-1][0],dp[i-1][2]),cost[i][2]+min(dp[i-1][0],dp[i-1][1])])
print(min(dp[n-1]))