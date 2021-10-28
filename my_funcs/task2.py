# Задание №2
# Запросить у пользователя координаты x и y двух точек на плоскости.
# Посчитать расстояние между заданными точками и вывести результат на консоль с точностью до трёх
# знаков после запятой (плавающей точки).

def function_coordinates(first_function_x, first_function_y, second_function_x, second_function_y):
    try:
        return float('{:.3f}'.format((((int(second_function_x) - int(first_function_x)) ** 2) + ((int(second_function_y) - int(first_function_y)) ** 2)) ** 0.5))
    except ValueError:
        print('Неверные входные данные')
