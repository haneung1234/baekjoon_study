# 16139

import sys
input = sys.stdin.readline

monja = input().strip() # 문자열 길이 정확하게 측정
q = int(input())

# len + 1임... 0부터 시작
prefix = [[0] * (len(monja) + 1) for _ in range(26)]

for i, ch in enumerate(monja):
    for j in range(26):
        prefix[j][i+1] = prefix[j][i] + (1 if ord(ch) - ord('a') == j else 0)

for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    idx = ord(a) - ord('a')
    print(prefix[idx][r+1] - prefix[idx][l])
