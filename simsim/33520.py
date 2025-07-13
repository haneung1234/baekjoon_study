# 33520

import sys
input = sys.stdin.readline

N = int(input())
a_max = 0
b_max = 0

for _ in range(N):
    a, b = map(int, input().split())
    small = min(a, b)
    large = max(a, b)
    a_max = max(a_max, small)
    b_max = max(b_max, large)

print(a_max * b_max)
