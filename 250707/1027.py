# 1027

num = int(input())
APT = list(map(int, (input().split())))

maxx = 0
for i in range(num):
  apt = 0

  if i != num-1:
    apt += 1
    gi = APT[i+1] - APT[i]
    for j in range(i+2, num):
      if ((APT[j] - APT[i])/ (j-i)) > gi:
        gi = (APT[j] - APT[i])/ (j-i)
        apt+=1
    
  if i != 0:
    apt += 1
    gi = APT[i] - APT[i-1]
    for j in range(i-2, -1, -1):
      if ((APT[j] - APT[i])/ (j-i)) < gi:
        gi = (APT[j] - APT[i])/ (j-i)
        apt+=1

  maxx = max(maxx, apt)
print(maxx)
