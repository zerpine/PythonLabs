line = input('Введите строку, состоящую из букв латинского алфавита ')
line_list = list(line)
duplicate = []
for item in line_list:
    if line_list.count(item) > 1 and item not in duplicate:
        duplicate.append(item)
        numbers = line_list.count(item)
        duplicate.append(numbers)
    elif line_list.count(item) == 1:
        duplicate.append(item)
print(''.join(map(str, duplicate)))