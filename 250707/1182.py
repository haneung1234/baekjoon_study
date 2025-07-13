# 1182

N, S = map(int, input().split())
num_list = list(map(int, input().split()))


def sub_sum(i, hap):
  if i == N:
    if hap == S:
      return 1
    return 0
  return sub_sum(i+1, hap + num_list[i]) + sub_sum(i+1, hap)


dap = sub_sum(0,0)

if S == 0:
  dap -= 1

print(dap)
