# Задание №3
# На ферме есть куры, коровы и свиньи. У курицы две ноги, у свиньи - четыре, у коровы - четыре.
# Запросить у пользователя (фермера) ввод кол-ва кур, свиней и коров,
# просуммировать кол-во ног всех животных и вывести результат на консоль.

def number_of_legs(number_of_chickens, number_of_pigs, number_of_cows):
    try:
        return int(number_of_chickens) * 2 + (int(number_of_pigs) + int(number_of_cows)) * 4
    except ValueError:
        print('Неверные входные данные')


