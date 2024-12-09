#Написать программу, которая:
#1.Создаёт случайный список из 20 значений по 4 случайных целых чисел от -10 до 10.
#2.Находит все уникальные комбинации пар из этих значений и выводит их в виде списка кортежей.
#3.Пользователь вводит целое число.
#4.Вычисляет количество пар, чья сумма меньше заданного пользователем значения.


import random
arr = [[random.randint(-10,10) for i in range(4)]for j in range(20)]

arr_2 = list()

for i in arr:
    i.sort()

for el in arr:
    if arr.count(el) == 1:
        x = tuple(el)
        arr_2.append(x)


print("Уникальные комбинации:")
print(arr_2)

count = 0

x = int(input("Введите число: "))

for tuple in arr_2:
    sum=0
    for el in tuple:
        sum+=el
    if sum < x:
        count+=1

print("Количествово пар, чья сумма меньше:",count)