# 25192

import sys
input = sys.stdin.readline

N = int(input())

chat_set = set()
suum = 0
for _ in range(N):
    who = input().strip()
    if who == "ENTER":
        suum += len(chat_set)
        chat_set = set()
    else:
        chat_set.add(who)
suum += len(chat_set)
print(suum)
