#2667

def coloring(lili, i, j, k, count):
  lili[i][j] = str(k)
  count += 1
  if(lili[i][j+1] == '1'):
    count = coloring(lili, i, j+1, k, count)
  if(lili[i+1][j] == '1'):
    count = coloring(lili, i+1, j, k, count)
  if(lili[i-1][j] == '1'):
    count = coloring(lili, i-1, j, k, count)
  if(lili[i][j-1] == '1'):
    count = coloring(lili, i, j-1, k, count)
  return count


num = int(input())
lili = []
coco = []

lili.append(['0'] * (num + 2)) 
for _ in range(num):
    lili.append(list('0' + input() + '0')) 
lili.append(['0'] * (num + 2)) 


k = 2

for i in range(1,num+1):
  for j in range(1,num+1):
    if(lili[i][j] == '1' and lili[i][j-1] == '0' and lili[i-1][j] == '0'):
      count = 0
      count = coloring(lili, i, j, k, count)
      coco.append(count)
      k+=1

coco.sort()

print(len(coco))
for _ in range(len(coco)):
  print(coco[_])
