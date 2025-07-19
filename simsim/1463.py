# 1463

N = int(input())
dp = [0] * (N+1)
dp[0] = float('inf')
dp[1] = 0
for i in range(2, N+1):
  one = 0
  two = 0
  three = i-1
  if i%3 == 0:
    one = i//3
  if i%2 == 0:
    two = i//2
  dp[i] = min(dp[one], dp[two], dp[three]) + 1

print(dp[N])
