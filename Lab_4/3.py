def GetDublicatesCount(elem_list):
    elem_dict = dict()
    for elem in elem_list:
        if elem in elem_dict:
            elem_dict[elem] += 1
        else:
            elem_dict[elem] = 1
    return elem_dict

elem_list = list(map(str, input("Введите элементы:").split()))
elem_dict = GetDublicatesCount(elem_list)
result = list(elem_dict.values())
print(*result, sep = " ")
