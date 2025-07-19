# 17219

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
st_pw = {}
for _ in range(N):
  site, pw = map(str, input().split())
  st_pw[site] = pw

for _ in range(M):
  ss = input().strip()
  print(st_pw[ss])
