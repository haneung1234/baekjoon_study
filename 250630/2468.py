# 2468

import sys
sys.setrecursionlimit(100000)
# 파이썬은 재귀를 1000번 정도만 가능하다고 함 -> sys로 우리가 늘려줘야함

def coloring(lili, i, j, k, count):
  lili[i][j] = k
  count += 1
  if(101>lili[i][j+1] > pp):
    count = coloring(lili, i, j+1, k, count)
  if(101>lili[i+1][j] > pp):
    count = coloring(lili, i+1, j, k, count)
  if(101>lili[i-1][j] > pp):
    count = coloring(lili, i-1, j, k, count)
  if(101>lili[i][j-1] > pp):
    count = coloring(lili, i, j-1, k, count)
  return count


num = int(input())

maxx = 0
lili = []
lili.append([0] * (num + 2))
for _ in range(num):
  tm = list(map(int, input().split()))
  tm = [0] + tm + [0]
  lili.append(tm)
  maxx = max(max(tm), maxx)
lili.append([0] * (num + 2))

answer = 0

for pp in range(maxx+1):
  temp = [row[:] for row in lili]
  k = 1000
  coco = []
  for i in range(1,num+1):
    for j in range(1,num+1):
      if( pp<temp[i][j] <101 ):
        count = 0
        count = coloring(temp, i, j, k, count)
        coco.append(count)
        k+=1
  answer = max(answer, len(coco))

print(answer)
