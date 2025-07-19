# 2745

N, B = map(str, input().split())
B = int(B)
hap = 0
for i in range(1, len(N)+1):
  if N[-i].isdigit():
    hap += int(N[-i])*(B**(i-1))
  else:
    hap += (ord(N[-i])-55)*(B**(i-1))
print(hap)
