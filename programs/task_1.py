#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


def test():
    n = int(input("Введите число: "))

    if n < 0:
        negative()

    elif n > 0:
        positive()


if __name__ == '__main__':
    test()