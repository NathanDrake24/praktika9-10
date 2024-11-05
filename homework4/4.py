def main():
    s = []
    while True:
        try:
            a = input("Введите целые число либо 'end' для завершения ввода: ")
            if a == 'end':
                break
            s.append(int(a))

        except ValueError:
            print("Ошибка: пожалуйста, введите корректные целые числа.")
    k = 0
    n = 0
    for i in range(0, len(s)):
        if s[i] % 2 != 0:
            n += 1
        if s[i] % 2 == 0:
            k += 1
    result = ', '.join(str(item) for item in s)
    print(f'Список введенных чисел: {result} \nКоличество четных элементов списка: {k} \n'
          f'Количество нечетных элементов списка: {n}')


if __name__ == '__main__':
    main()