import sys


def main():
    s = []
    for line in sys.stdin:
        try:
            a = line.strip()
            if a == 'end':
                break
            s.append(int(a))
        except ValueError:
            print("Ошибка: пожалуйста, введите корректные целые числа.")

    uneven = [num for num in s if num % 2 != 0]
    result = ', '.join(str(item) for item in uneven)

    print(f'Нечетные числа среди введенных: {result} ')

if __name__ == '__main__':
    main()