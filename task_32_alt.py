# Задача 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше 
# заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
from random import randint

list_ = [randint(-10, 10) for i in range(int(input('Enter size of list: ')))]
border = list(map(int, (input("Enter a range of numbers using a spacebar: ").split())))
new_list = print([i for i in range(len(list_)) if border[0] <= list_[i] <= border[1]])