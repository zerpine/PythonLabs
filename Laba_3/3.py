import sys
num, num1, num2, num3 = int(input('Введите число ')), 0, 0, 0
num3 = num % 10
num2 = (num // 10) % 10
num1 = num // 100
num3_dict = dict([(1, 'один'), (2, 'два'), (3, 'три'), (4, 'четыре'), (5, 'пять'), (6, 'шесть'), (7, 'семь'),
                  (8, 'восемь'), (9, 'девять'), (0, '')])
num2_dict = dict([(2, 'двадцать'), (3, 'тридцать'), (4, 'сорок'), (5, 'пятьдесят'), (6, 'шестьдесят'),
                  (7, 'семьдесят'), (8, 'восемьдесят'), (9, 'девяносто'), (0, '')])
num1_dict = dict([(1, 'сто'), (2, 'двести'), (3, 'триста'), (4, 'четыреста'), (5, 'пятьсот'), (6, 'шестьсот'),
                  (7, 'семьсот'), (8, 'восемьсот'), (9, 'девятьсот'), (0, '')])
if num == 0:
    print('ноль')
    sys.exit()
elif num == 10:
    print('десять')
    sys.exit()
elif num == 11:
    print('одиннадцать')
    sys.exit()
elif num == 12:
    print('двенадцать')
    sys.exit()
elif num == 13:
    print('тринадцать')
    sys.exit()
elif num == 14:
    print('четырнадцать')
    sys.exit()
elif num == 15:
    print('пятнадцать')
    sys.exit()
elif num == 16:
    print('шестнадцать')
    sys.exit()
elif num == 17:
    print('семнадцать')
    sys.exit()
elif num == 18:
    print('восемьнадцать')
    sys.exit()
elif num == 19:
    print('девятнадцать')
    sys.exit()
if num1 != 0 and num2 != 0 and num3 != 0:
    print(num1_dict[num1] + ' ' + num2_dict[num2] + ' ' + num3_dict[num3])
elif num1 == 0 and num2 != 0 and num3 != 0:
    print(num2_dict[num2] + ' ' + num3_dict[num3])
else:
    print(num3_dict[num3])