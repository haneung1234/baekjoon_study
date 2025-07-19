# 22115

N, K = map(int, input().split())
coffee = list(map(int, input().split()))

dp = [float('inf')] * (K + 1)
dp[0] = 0

for c in coffee:
    for i in range(K, c - 1, -1):
        dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[K] if dp[K] != float('inf') else -1)
