# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# d = √ [(x2-x1)2 + (y2-y1)2]

from math import*
x1 = float(input('Введите значение x1:'))
y1 = float(input('Введите значение y1:'))
x2 = float(input('Введите значение x2:'))
y2 = float(input('Введите значение y2:'))
d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 
print (d)