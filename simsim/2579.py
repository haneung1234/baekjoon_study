# 2579

N = int(input())

st = [0]

for i in range(N):
  st.append(int(input().strip()))

dp = [[0, 0], [st[1], st[1]]]

# dp[i][0 or 1] i번째 계단이 0이면 직전에서 올라온거 1이면 전전에서 올라온거

for i in range(2, N+1):
  temp = []
  temp.append(st[i] + dp[i-1][1])
  temp.append(st[i] + max(dp[i-2][0], dp[i-2][1]))
  dp.append(temp)

print(max(dp[N]))
