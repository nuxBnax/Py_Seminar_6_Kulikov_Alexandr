# Задача 30:
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: 

# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# list_con = []
# list_str = (input("Введите последовательность трех чисел: ").split())
list_int = list(map(int, (input("Enter a numbers using a spacebar for progression an = a1 + (n-1) * d: ").split())))

for item in range(1, list_int[2] + 1):
    progression = list_int[0] + (item-1) * list_int[1]
    print(progression, end=' ')
