"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать программу, которая будет выводить количество четных и нечетных значений
в списке из целых чисел

even - четные
odd - нечетные
"""


def calc_even_odd(array: list) -> tuple:

    counter_1 = 0
    counter_2 = 0
    for i in array:
        if i % 2 == 0:
            counter_1 = counter_1 + 1
        else:
            counter_2 = counter_2 + 1

    return counter_1, counter_2


if __name__ == '__main__':
    assert calc_even_odd([2, 1, 5, 4, 7]) == (2, 3)
    print('Решено!')
