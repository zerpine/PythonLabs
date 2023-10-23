with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]

sortedn = list(map(int, lines))
sortedn.sort()
res = list(map(str, sortedn))

with open('output.txt', 'w') as f:
    f.writelines(f"{item}\n" for item in res)