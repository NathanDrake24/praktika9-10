import re


def parse_email(email):
    # Регулярное выражение для захвата имени пользователя и домена
    pattern = r"^(?P<username>[a-zA-Z0-9._%+-]+)@(?P<domain>[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$"
    match = re.match(pattern, email)

    if match:
        username = match.group("username")
        domain = match.group("domain")
        print(f"username: {username}")
        print(f"domain: {domain}")
    else:
        print("Некорректный email. Попробуйте снова.")


def main():
    while True:
        email = input("Введите email (или 'stop' для завершения): ")
        if email.lower() == "stop":
            print("Завершение программы.")
            break
        parse_email(email)


if __name__ == "__main__":
    main()
