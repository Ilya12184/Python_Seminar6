# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

list_1 = []
for i in range(15):
    list_1.append(random.randint(-10, 10))
print(list_1)

min_number = int(input('Минимальное значение интервала: '))
max_number = int(input('Максимальное значение интервала: '))

list_2 = []
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        list_2.append(i)
print('Индексы элементов, входящие в заданный интервал', list_2)
