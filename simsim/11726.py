# 11726

n = int(input())

sq = [0] * (n + 2)  
sq[1] = 1
sq[2] = 2

for i in range(3, n + 1):
    sq[i] = (sq[i - 1] + sq[i - 2])

print(sq[n]% 10007)
