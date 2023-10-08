line = input('Введите строку содержающую буквы из латинского алфавита и числа ')
line_list = list(line)
summary = len(line_list)
result = ''
for i in range(summary-1):
    if line_list[i].isnumeric() and line_list[i+1].isnumeric():
        new_value = line_list[i] + line_list[i+1]
        temp = i
        del line_list[i]
        del line_list[i]
        line_list.insert(temp, new_value)
summary = len(line_list)
for i in range(summary-1):
    if line_list[i].isnumeric() == False and line_list[i+1].isnumeric() == True:
        result += line_list[i] * int(line_list[i + 1])
    elif line_list[i].isnumeric() == True and line_list[i+1].isnumeric() == False:
        result += line_list[i + 1]
    elif line_list[i].isnumeric() == False and line_list[i+1].isnumeric() == False:
        result += line_list[i + 1]
print(result)