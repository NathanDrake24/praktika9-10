import random

size = random.randint(5, 10)
s = []
for k in range(size):
    if random.choice([True, False]):
        n = round(random.uniform(-10, 10), 2)
    else:
        n = random.randint(-10, 10)
    s.append(n)
min = s.index(min(s))
max = s.index(max(s))
print("Исходный список:", s)
minn = s[min]
maxn = s[max]
s[min] = maxn
s[max] = minn
print("Измененный список, после замены максимального элемента на минимальный и минимального на максимальный: ", s)
