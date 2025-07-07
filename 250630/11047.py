#11047

N, K = map(int, input().split())
money = []
getsu = 0

for _ in range(N):
  m = int(input())
  if m <= K:
    money.append(m)

for i in range(1,len(money)+1):
  # if를 안 써도 되지 않을까?? 비교 vs 연산의 시간 복잡도를 생각하면 좋겠다~
  if K >= money[-i]:
    getsu += K // money[-i]
    K = K % money[-i]

print(getsu)
