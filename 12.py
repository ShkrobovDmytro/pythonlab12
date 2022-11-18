from sympy import *
import numpy as np
import math


def rd(x, y = 0):
    m = int('1'+'0'*y)
    q = x * m
    a = int(q)
    i = int((q - a) * 10)
    if i >= 5:
        a += 1
    return a/m


def rectangles():
    a = float(input("Введите нижнюю границу интегрирования "))
    b = float(input("Введите верхнюю границу интегрирования "))
    n = int(input("Введите n "))
    y = input("Введите подинтегральную функцию ")
    h = rd((b - a) / n, 3)
    print(f"h={h}")

    aleft = a
    bleft = b - h
    summ = 0
    while aleft <= bleft + h / 2:
        x = aleft
        summ += eval(y)
        aleft += h
    print(f"∫({y})dx≈{rd(summ * h, 4)} - по формуле левых прямоугольников")

    aright = a + h
    bright = b
    summ = 0
    while aright <= bright + h / 2:
        x = aright
        summ += eval(y)
        aright += h
    print(f"∫({y})dx≈{rd(summ * h, 4)} - по формуле правых прямоугольников")

    acenter = a + h / 2
    bcenter = b - h / 2
    summ = 0
    while acenter <= bcenter + h / 4:
        x = acenter
        summ += eval(y)
        acenter += h
    print(f"∫({y})dx≈{rd(summ * h, 4)} - по формуле средних прямоугольников")
    return 0


def trapezoid():
    a = float(input("Введите нижнюю границу интегрирования "))
    b = float(input("Введите верхнюю границу интегрирования "))
    n = int(input("Введите n "))
    y = input("Введите подинтегральную функцию ")
    h = rd((b - a) / n, 3)
    print(f"h={h}")

    summ = 0
    i = 0
    while a <= b + h / 2:
        x = a
        y1 = eval(y)
        if i == 0 or i == n:
            y1 /= 2
        summ += y1
        i += 1
        a += h
    print(f"∫({y})dx≈{rd(summ * h, 4)} - по методу трапеции")
    return 0


def simpson():
    a = float(input("Введите нижнюю границу интегрирования "))
    b = float(input("Введите верхнюю границу интегрирования "))
    n = int(input("Введите n "))
    y = input("Введите подинтегральную функцию ")
    h = rd((b - a) / n, 3)
    print(f"h={h}")

    summ = 0
    i = 0
    while a <= b + h / 2:
        x = a
        y1 = eval(y)
        if i % 2 == 0 and i != 0 and i != n:
            y1 *= 2
        elif i % 2 != 0 and i != 0 and i != n:
            y1 *= 4
        summ += y1
        i += 1
        a += h
    print(f"∫({y})dx≈{rd(summ * h / 3, 4)} - по методу Симпсона")
    return 0


while True:
    x = int(input("Введите 1 для метода прямоугольников, 2 - для Симпсона, 3 - для трапеций "))
    if x == 1:
        rectangles()
    elif x == 2:
        simpson()
    elif x == 3:
        trapezoid()
    else:
        print("Неверный ввод ")
        continue


