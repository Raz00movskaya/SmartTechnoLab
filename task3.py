# Задание №3
# На ферме есть куры, коровы и свиньи. У курицы две ноги, у свиньи - четыре, у коровы - четыре.
# Запросить у пользователя (фермера) ввод кол-ва кур, свиней и коров,
# просуммировать кол-во ног всех животных и вывести результат на консоль.
number_of_chickens = int(input('Введите кол-во кур: '))
number_of_pigs = int(input('Введите кол-во свиней: '))
number_of_cows = int(input('Введите кол-во коров: '))
print('Кол-во ног животных: ', (number_of_chickens * 2 + (number_of_pigs + number_of_cows) * 4))