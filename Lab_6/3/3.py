file = open('input.txt', encoding='utf-8')
s = file.readlines()
file.close()

data = []
for i in s:
    data.append(i.strip())

MyList = []
for line in data:
    MyList.append(line.split())

data.clear()

MyList.sort(key=lambda x: x[2])

for i in MyList:
    data.append(' '.join(map(str, i)))
print(data)

f1 = open('youngest.txt', 'w', encoding='utf-8')
f1.write(data[0])
f1.close()

f2 = open('oldest.txt', 'w', encoding='utf-8')
f2.write(data[-1])
f2.close()