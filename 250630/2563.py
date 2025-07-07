# 2563

# 백준에서는 numpy 사용 불가 -> 직접 배열 만들어라~
matrix = [[0] * 100 for _ in range(100)]

num = int(input())
suum = 0

for _ in range(num):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      if matrix[i][j] == 0:
        suum += 1
        matrix[i][j] = 1

print(suum)
