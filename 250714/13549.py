# 13549
from collections import deque

soobin, dong = map(int, input().split())

dist = [float('inf')] * 100001
dist[soobin] = 0

Q = deque()
Q.append(soobin)
while Q:
  now = Q.popleft()
  if now == dong:
    print(dist[now])
    break
  node = now*2
  if (0<= node <= 100000) and (dist[node] > dist[now]):
    dist[node] = dist[now]
    Q.appendleft(node)
  for node in [now+1, now-1]:
    if (0<= node <= 100000) and (dist[node] > dist[now] + 1):
      dist[node] = dist[now]+1
      Q.append(node)
