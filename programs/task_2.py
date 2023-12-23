#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import pi


def circle(r):
    return pi*(r**2)


def cylinder():
    r = int(input("Введите радиус цилиндра: "))
    h = int(input("Введите высоту цилиндра: "))
    v = int(input("Введите 1, если вы хотите вычислить "+
                  "площадь боковой поверхности цилиндра.\n"+
                  "Введите любое другое число, если вы хотите"+
                  " вычислить полную площадь цилиндра\n"))
    
    if v == 1:
        print(f"Площадь боковой поверхности цилиндра равна: {2*pi*r*h}")
    elif v == 2:
        print(f"Полная площадь цилиндра равна: {2*pi*r*h + 2*circle(r)}")


if __name__ == '__main__':
    cylinder()