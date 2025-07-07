# 14891

def dir (wheel, num, bang):
  st = num
  fin = num
  dic = dict()
  dic[num-1] = bang 
  for i in range(num-1, 3):
    if wheel[i][2] == wheel[i+1][6]:
      fin = i
      break
    else:
      dic[i+1] = -dic[i]
  for i in range(num-1, 0 , -1):
    if wheel[i-1][2] == wheel[i][6]:
      st = i
      break
    else:
      dic[i-1] = - dic[i]
  for i in range(4):
    if i in dic:
      if dic[i] == -1:
        turnL(wheel[i])
      elif dic[i] == 1:
        turnR(wheel[i])

def turnL(LI):
  LI.append(LI[0]) 
  del(LI[0])

def turnR(LI):
  LI.insert(0, LI[-1]) 
  del(LI[-1])



wheel = []
for _ in range(4):
  get = input()
  wheel.append(list(get))


N = int(input())

for _ in range(N):
  num, bang = map(int, input().split())
  dir (wheel, num, bang)

score = 0

for i in range(4):
  if wheel[i][0] == "1":
    score += 2**i

print(score)
