# Программа, которая принимает номер четверти в системе координат и выдает все возможные
# значения координат X и Y в данной четверти
user_number = int(input ("Введите номер четверти в системе координат (от 1 до 4): "))
if user_number == 1:
    print("x - от 0 до положительного бесконечно большого числа (не включая 0); y - от 0 до положительного бесконечно большого числа (не включая 0)")
if user_number == 2:
    print("x - от отрицательного бесконечно большого числа до 0 (не включая 0)); y - от 0 до положительного бесконечно большого числа (не включая 0)")
if user_number == 3:
    print("x и y - от отрицательного бесконечно большого числа до 0 (не включая 0)")
if user_number == 4:
    print("x - от положительного бесконечно большого числа до 0 (не включая 0)); y - от отрицательного бесконечно большого числа до 0 (не включая 0)")