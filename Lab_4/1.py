input_list = [int(el) for el in input().split()]
max_n = input_list.index(max(input_list))
min_n = input_list.index(min(input_list))
input_list[max_n], input_list[min_n] = input_list[min_n], input_list[max_n]
print(input_list)