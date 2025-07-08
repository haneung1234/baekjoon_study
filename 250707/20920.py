# 20920 

import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

word_dict = {}

for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

sorted_words = sorted(word_dict.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

for word, _ in sorted_words:
  print(word + '\n') 
