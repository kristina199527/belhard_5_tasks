"""
Написать функцию odd_sum, которая принимает список, который может состоять
из различных элементов.
Если все элементы списка целые числа, то функция должна посчитать сумму
нечетных чисел.
Если хотя бы один элемент не является целым числом, то выкинуть ошибку
TypeError с сообщением "Все элементы списка должны быть целыми числами"
Задачу стоит выполнить с помощью одного цикла

Написать блок if __name__ == '__main__', в котором
нужно описать обработку исключения try-except-else-finally
"""


def odd_sum(int_list: list) -> int:

    summa = 0
    for y in range(len(int_list)):
        if not isinstance(int_list[y], int):
            raise TypeError
        elif int_list[y] % 2 != 0:
            summa = summa + int_list[y]
    else:
        return summa


if __name__ == '__main__':
    some_list = [1, 2, 3, '123']
    try:
        odd_sum(some_list)
    except TypeError as exc:
        print(exc)
        print("Все элементы списка должны быть целыми числами")
    except ValueError as exc:
        print(exc)
        print("Все элементы списка должны быть целыми числами")
