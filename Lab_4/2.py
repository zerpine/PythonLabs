a = list(map(int, input('Введите первый список: ').split()))
b = list(map(int, input('Введите второй список: ').split()))
c = []
for i in a:
    if i in b and i not in c:
        c.append(i)
 
print("Количество одинаковых чисел:", len(c))
