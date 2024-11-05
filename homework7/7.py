import random

size = random.randint(5, 10)
s = []

for k in range(size):
    if random.choice([True, False]):
        n = round(random.uniform(-10, 10), 2)
    else:
        n = random.randint(-10, 10)
    s.append(n)

print("Список элементов до сдвига каждого элемента вправо: ", s)

if len(s) > 1:
    last = s[-1]
    for i in range(len(s) - 1, 0, -1):
        s[i] = s[i - 1]
    s[0] = last

print("Список элементов после сдвига каждого элемента вправо: ", s)
