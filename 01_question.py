"""
Задача 22: 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. 
n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.

"""

first_list = []
second_list = []

n = int(input('Enter first length: '))
m = int(input('Enter second length: '))

print('Enter numbers for the first list:')
for i in range(0, n):
    first_list.append(input(f'{i + 1} element: '))

print('Enter numbers for the second list:')
for i in range(0, m):
    second_list.append(input(f'{i + 1} element: '))

print('First list = ' , first_list)
print('Second list = ' , second_list)

some_set = set(first_list).intersection(set(second_list))

final_list = list(some_set)
final_list.sort()

print('Final result: ', final_list)