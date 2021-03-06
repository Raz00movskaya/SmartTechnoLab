# Задание №6
# Вы получаете ввод числа от пользователя. Построить цикл от нуля до введенного числа (включительно)
# и посчитать сумму всех чисел, делимых без остатка на 3 или 5. Вывести это число на консоль.


def counter_of_nums(number_of_iterations):
    try:
        result = 0
        for i in range(int(number_of_iterations) + 1):
            if ((i % 3) == 0) or ((i % 5) == 0):
                result += i
        return result
    except ValueError:
        print('Неверные входные данные')
