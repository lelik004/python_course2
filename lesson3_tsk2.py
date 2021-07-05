"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random

START = 0
FINISH = 100
LENGTH = 10

main_list = [random.randint(START, FINISH) for _ in range(LENGTH)]
print(f'Исходный массив: {main_list}')
temp_list = main_list.copy()
finish_list = []

for i in main_list:
    if i % 2 == 0:
        index_i = temp_list.index(i)
        finish_list.append(index_i)

        """
        Изменяем на None элемент, удовлетваряющий поиску. Чтобы в случае повторения четного чисела, корректно 
        определить индекс последующих за первым повторяющимся четным.
        """
        temp_list[index_i] = None

print(f'Список индексов четных чисел исходного массива: {finish_list}')