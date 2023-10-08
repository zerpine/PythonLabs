line_list = list(input('Введите строку'))
n_l = []
line_list_no_dupl = []
number = 1
length = len(line_list)

for i in range(length-1):
    if line_list[i] == line_list[i + 1]:
        number += 1
    else:
        n_l.append(number)
        number = 1
        line_list_no_dupl.append(line_list[i])


n_l.append(number)
line_list_no_dupl.append(line_list[-1])
dictionary = dict(zip(line_list_no_dupl, n_l))
sorted_dictionary = sorted(dictionary.items(), key = lambda item: item[1], reverse=True)

for i in range(3):
    print(*sorted_dictionary[i])
