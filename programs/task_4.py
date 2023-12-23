#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n = input()
    return n


def test_input(n):
    return n.isdigit()


def str_to_int(n):
    return int(n)


def print_int(n):
    print(n)


if __name__ == '__main__':
    n = get_input()
    b = test_input(n)
    
    if b == True:
        n_int = str_to_int(n)
        print_int(n_int)