#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
print('Для установленного заданием списка [1.1, 1.2, 3.1, 5, 10.01]:')
my_list = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in my_list:
    if (i - int(i)) <= min and i != int(i):
        min = i - int(i)
    if (i - int(i)) >= max and i != int(i):
        max = i - int(i)
print(f'Разница между максимальным {round(max, 2)} и минимальным {round(min, 2)} значением дробной части элементов = {round(max-min, 2)}')
print()
print('Для произвольных чисел, вводимых пользователем.')
print('Вы введете несколько чисел, в том числе с дробными частями, я найду разцицу между максимальным и минимальным значением дробной части элементов.')
my_list = list(map(float, input('Введите дробные числа через пробел, используйте . (точку) как разделитель дробной части: \n').split()))
min = 1
max = 0
for i in my_list:
    if (i - int(i)) <= min and i != int(i):
        min = i - int(i)
    if (i - int(i)) >= max and i != int(i):
        max = i - int(i)
print(f'Разница между максимальным {round(max, 2)} и минимальным {round(min, 2)} значением дробной части элементов = {round(max-min, 2)}')