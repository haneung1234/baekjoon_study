# 2042

import sys
input = sys.stdin.readline

N, M, K  = map(int, input().split())
nums = [0]
for i in range(N):
  get = int(input().strip())
  nums.append(get)

size = 1
while size < N:
  size *= 2

tree = [0] * (2 * size)


for i in range(1, N+1):
  tree[size + i - 1] = nums[i]

for i in range(size - 1, 0, -1):
  tree[i] = tree[2 * i] + tree[2 * i + 1]

def update(b, c):
  pos = size + b - 1
  tree[pos] = c
  while pos > 1:
    pos //= 2
    tree[pos] = tree[2 * pos] + tree[2 * pos + 1]

def query(b, c):
  b = b + size - 1
  c = c + size - 1
  total = 0
  while b <= c:
    if b % 2 == 1:
      total += tree[b]
      b += 1
    if c % 2 == 0:
      total += tree[c]
      c -= 1
    b //= 2
    c //= 2
  return total

for _ in range(M + K):
  a, b, c = map(int, input().split())
  if a == 1:
    update(b, c)
  else:
    print(query(b, c))
