# 10828 
import sys

def push(soo):
  lili.append(soo)

def pop():
  if len(lili) == 0:
    print(-1)
  else:
    print(lili[-1])
    del(lili[-1])

def size():
  print(len(lili))

def empty():
  if len(lili) == 0:
    print(1)
  else:
    print(0)

def top():
  if len(lili) == 0:
    print(-1)
  else:
    print(lili[-1])



input = sys.stdin.readline
num = int(input())
lili = []

for _ in range(num):
  get = input().split()
  one = get[0]

  if one == "push":
    push(int(get[1])) # push일때만 2개를 입력 받음 -> push일때만 변환
  elif one == "pop":
    pop()
  elif one == "size":
    size()
  elif one == "empty":
    empty()
  elif one == "top":
    top()
