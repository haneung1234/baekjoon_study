# 14503

import sys
input = sys.stdin.readline

def back(avail, r, c, d):
  if d == 0 and r + 1 < N and room[r+1][c] != 1:
    r = r+1
    avail = 1
  elif d == 1 and c - 1 >= 0 and room[r][c-1] != 1:
    c = c-1
    avail = 1
  elif d == 2 and r - 1 >= 0 and room[r-1][c] != 1:
    r = r-1
    avail = 1
  elif d == 3 and c + 1 < M and room[r][c+1] != 1:
    c = c+1
    avail = 1
  return avail, r, c, d

def front(r, c, d):
  if d == 0 and r - 1 >= 0 and room[r-1][c] == 0:
    r = r-1
  elif d == 1 and c + 1 < M and room[r][c+1] == 0:
    c = c+1
  elif d == 2 and r + 1 < N and room[r+1][c] == 0:
    r = r+1
  elif d == 3 and c - 1 >= 0 and room[r][c-1] == 0:
    c = c-1
  return r, c, d


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for i in range(N):
  get = list(map(int, input().split()))
  room.append(get)

clean = 0

while True:
  if room[r][c] == 0:
    room[r][c] = 2
    clean += 1
  if (r + 1 >= N or room[r+1][c] != 0) and (r - 1 < 0 or room[r-1][c] != 0) and (c + 1 >= M or room[r][c+1] != 0) and (c - 1 < 0 or room[r][c-1] != 0):
    avail = 0
    avail, r, c, d = back(avail, r, c, d)
    if avail == 0:
      break
  else:
    d = (d+3)%4
    r, c, d = front(r, c, d)

print(clean)
