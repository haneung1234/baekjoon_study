# 2805

N, M = map(int, input().split())
namu = list(map(int, input().split()))


minn = 0
maxx = max(namu)

dap = 0

while minn <= maxx:
  mid = (minn + maxx) // 2
  summ = 0
  for height in namu:
    if height > mid:
      summ += (height - mid)
  if summ >= M:
    minn = mid + 1
    dap = mid
  elif summ < M:
    maxx = mid - 1

print(dap)
