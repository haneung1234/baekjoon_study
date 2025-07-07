# 26069

num = int(input())

li = ['ChongChong']

for _ in range(num):
  a, b = map(str, input().split())
  if (a in li) and not(b in li):
    li.append(b)
  elif (b in li) and not(a in li):
    li.append(a)

print(len(li))
