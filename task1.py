# Программа, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным

user_number = int(input("Введите порядковый номер дня недели (от 1 до 7): "))
if user_number >= 1 and user_number <= 7:
    if user_number <= 5:
        print(f"- {user_number} -> нет")
    else:
        print(f" - {user_number} - да")
else:
    print("Введено неверное число")