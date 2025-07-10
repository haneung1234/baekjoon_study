# 1260

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M, V = map(int, input().split())

node_dic = {i: [] for i in range(1, N + 1)}

for _ in range(M):
  a, b = map(int, input().split())
  node_dic[a].append(b)
  node_dic[b].append(a)

for key in node_dic.keys():
  node_dic[key].sort()

# DFS
def DFS():
  if len(DFS_list) == 0:
    return
  node = DFS_list[-1]
  del(DFS_list[-1])
  DFS_fi_list.append(node) 
  print(node, end = " ")
  for i in range(len(node_dic[node])):
    if not (node_dic[node][i] in DFS_fi_list or node_dic[node][i] in DFS_list):
      DFS_list.append(node_dic[node][i])
      DFS() 

# BFS
def BFS():
  if len(BFS_list) == 0:
    return
  node = BFS_list[0]
  del(BFS_list[0])
  BFS_fi_list.append(node)
  print(node, end = " ")
  for i in range(len(node_dic[node])):
    if not (node_dic[node][i] in BFS_fi_list or node_dic[node][i] in BFS_list):
      BFS_list.append(node_dic[node][i])
  BFS()


DFS_list = [V]
DFS_fi_list = []
DFS()
print()
BFS_list = [V]
BFS_fi_list = []
BFS()
