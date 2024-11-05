import random


def main():
    size = random.randint(1, 100)
    numbers = []

    for k in range(size):
        if random.choice([True, False]):
            number = round(random.uniform(-10, 10), 2)
        else:
            operation = random.choice(["cube", "square_root"])
            if operation == "cube":
                number = round(random.uniform(-5, 5) ** 3, 2)
            elif operation == "square_root":
                number = round(random.uniform(0, 10) ** 0.5, 2)
        numbers.append(number)

    result = []
    for i in range(1, size):
        if numbers[i] > numbers[i - 1]:
            result.append(numbers[i])

    print("Исходный список:", numbers)
    print("Элементы, которые больше предыдущего:", result)


if __name__ == '__main__':
    main()
