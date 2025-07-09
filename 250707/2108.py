# 2108

import sys
input = sys.stdin.readline

num = int(input())

number = []
number_d = {}
for _ in range (num):
  tt = int(input())
  number.append(tt)
  if not(tt in number_d):
    number_d[tt] = 1
  else:
    number_d[tt] += 1

number.sort()


number_d = dict(sorted(number_d.items(), key =lambda item : item[1], reverse = True))
mode = []
gg = -1
for key in number_d.keys():
  if gg == -1:
    mode.append(key)
    gg = number_d[key]
  elif gg == number_d[key]:
    mode.append(key)
  else:
    break
mode.sort() 

if len(mode) >=2:
  gg = mode[1]
else:
  gg = mode[0]

print(round(sum(number)/num))
print(number[num//2])
print(gg)
print(max(number)-min(number))
