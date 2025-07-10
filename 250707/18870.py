# 18870

num = int(input())
number_list = list(map(int, input().split()))
sorted_number_list = sorted(set(number_list))

getsu_dict = {}
i = 0
for key in sorted_number_list:
  getsu_dict[key] = i
  i+=1
  
for key in number_list:
  print(getsu_dict[key], end = " ")
