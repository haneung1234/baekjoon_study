# 7576

from collections import deque
import sys
input = sys.stdin.readline

def tomatomato():
  Q = deque()
  for i in range(N):
    for j in range(M):
      if box[i][j] == 1:
        Q.append((i, j, 0))

  max_day = 0

  while Q:
    x, y, day = Q.popleft()
    max_day = max(max_day, day)

    if x > 0 and box[x-1][y] == 0:
      box[x-1][y] = 1
      Q.append((x-1, y, day + 1))

    if x < N-1 and box[x+1][y] == 0:
      box[x+1][y] = 1
      Q.append((x+1, y, day + 1))

    if y > 0 and box[x][y-1] == 0:
      box[x][y-1] = 1
      Q.append((x, y-1, day + 1))

    if y < M-1 and box[x][y+1] == 0:
      box[x][y+1] = 1
      Q.append((x, y+1, day + 1))

  return max_day


M, N = map(int, input().split())
box = []
for _ in range(N):
  get = list(map(int, input().split()))
  box.append(get)


maxx = tomatomato()

da = 0
for i in range(N):
  if 0 in box[i]:
    da = -1
    break

if da == -1:
  print(-1)
else:
  print(maxx)
