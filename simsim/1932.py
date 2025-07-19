# 1932

import sys
input = sys.stdin.readline

N = int(input())

tri = []

for i in range(N):
  get = list(map(int, input().split()))
  tri.append(get)

maxi = [tri[0]]
for i in range(1, N):
  temp = []
  temp.append(maxi[i-1][0]+tri[i][0])
  for j in range(1, i):
    temp.append(max(maxi[i-1][j-1], maxi[i-1][j])+tri[i][j])
  temp.append(maxi[i-1][i-1]+tri[i][i])
  maxi.append(temp)

print(max(maxi[N-1]))
