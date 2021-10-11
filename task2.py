# Задание №2
# Запросить у пользователя координаты x и y двух точек на плоскости.
# Посчитать расстояние между заданными точками и вывести результат на консоль с точностью до трёх
# знаков после запятой (плавающей точки).

function_coordinates = input('Введите координаты двух точек в формате x1 y1 x2 y2: ')
first_function_x = int(function_coordinates.split(" ")[0])
first_function_y = int(function_coordinates.split(" ")[1])
second_function_x = int(function_coordinates.split(" ")[2])
second_function_y = int(function_coordinates.split(" ")[3])
print('Расстояние между точками: ', '{:.3f}'.format((((second_function_x - first_function_x) ** 2) + ((second_function_y - first_function_y) ** 2)) ** 0.5))
