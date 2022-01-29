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
    for y in int_list:
        if type(y) is int and y % 2 != 0:
            summa = summa + y
        else:
            continue
    return summa


if __name__ == '__main__':
    some_list = [1, 2, 3, '123']
    try:
        for i in some_list:
            if type(i) is not int:
                raise TypeError(f' not int')

    except TypeError as exc:
        print(exc)
        print("Все элементы списка должны быть целыми числами")

