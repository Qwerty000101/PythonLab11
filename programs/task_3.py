#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def multiple():
    S = 1
    while True:
        n = int(input("Введите число: "))
        if n == 0:
            break

        S *= n
        print(f"Результат: {S}")


if __name__ == '__main__':
    multiple()