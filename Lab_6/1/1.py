file = open("input.txt")
num = file.readline().split()
file.close()
product = 1
num = list(map(int, num))
for s in num:
    product *= s
file1 = open("output.txt","w")
file1.write(str(product))
file1.close()