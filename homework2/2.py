def get_square_list(a, b):
    numbers = [i for i in range(int(min(a, b)), int(max(a, b)) + 1) if (i > a and i < b) or (i < a and i > b)]
    squares = list(map(lambda x: x**2, numbers))
    return numbers, squares


def main():
    while True:
        try:
            a = float(input("Введите число a: "))
            b = float(input("Введите число b: "))
            break
        except ValueError:
            print("Ошибка: пожалуйста, введите корректные числа.")

    numbers, squares = get_square_list(a, b)

    print(f"Квадраты целых чисел: {squares}")


if __name__ == '__main__':
    main()