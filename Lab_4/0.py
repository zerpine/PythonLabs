input_list = [int(el) for el in input().split()]
output_list = []
for i in range(len(input_list)-1):
    if input_list[i] < input_list[i+1]:
        output_list.append(input_list[i+1])
    i += 1
if len(output_list)>=1:
    print(output_list)
else:
    print("Элементы не найдены")