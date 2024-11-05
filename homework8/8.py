import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def get_ticket():
    user_ticket = []
    print("Введите по одному числу из каждой строки лотерейного билета:")
    while True:
        for i, row in enumerate(ticket):
            num = input(f"Введите число из строки {i + 1} {row}: ")
            while True:
                if not num.isdigit():
                    num = input("Ошибка. Введите только цифры: ")
                elif int(num) not in row:
                    num = input("Ошибка. Введите число из указанной строки: ")
                else:
                    user_ticket.append(int(num))
                    break
        # Проверка на то, что введены числа только из одной строки билета
        if len(set(user_ticket)) == len(user_ticket):
            break
        else:
            print("Введите по одному числу из каждой строки лотерейного билета.")
            user_ticket = []
    return user_ticket

def generate_ticket():
    return [random.choice(row) for row in ticket]

# Бесконечный цикл для ввода и проверки чисел
while True:
    user_ticket = get_ticket()
    random_ticket = generate_ticket()

    print(f"nВаш лотерейный билет: {user_ticket}")
    print(f"Случайно сгенерированный билет: {random_ticket}")

    matches = set(user_ticket) & set(random_ticket)
    if matches:
        print(f"Количество совпадений: {len(matches)}")
        print(f"Совпадения: {matches}")
    else:
        print("Нет совпадений")
