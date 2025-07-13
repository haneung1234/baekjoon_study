# 1699

N = int(input())
zegop = [0] * (N+1)

for i in range(1, N+1):
    zegop[i] = i  
    j = 1
    while j*j <= i:
        zegop[i] = min(zegop[i], zegop[i - j*j] + 1)
        j += 1

print(zegop[N])
