# 1149

import sys
input = sys.stdin.readline

N = int(input())

cost = []

for i in range(N):
  get = list(map(int, input().split()))
  cost.append(get)

# dp[i][color]: i번째가 color일때 비용 담는 (color은 0R, 1G, 2B 라 하자)

dp = []
for i in range(N):
  dp.append([1001, 1001, 1001])

for i in range(3):
  dp[0][i] = cost[0][i]

for i in range(1, N):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
  dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + cost[i][2]

print(min(dp[N-1]))
