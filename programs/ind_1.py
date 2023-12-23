#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def add():
    '''
    Добавить маршрут
    '''
    name_start = input("Начальный пункт маршрута? ")
    name_end = input("Конечный пункт маршрута? ")
    number = int(input("Номер маршрута? "))

    route = {
            'name_start': name_start,
            'name_end': name_end,
            'number': number,
            }
    
    return route


def list(routes):
    '''
    Вывести список маршрутов
    '''
    if routes:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 30,
                '-' * 8
                )
        print(line)

        print('| {:^4} | {:^30} | {:^30} | {:^8} |'.format(
                "№",
                "Начальный пункт",
                "Конечный пункт",
                "Номер"
                )
              )
        print(line)

        for idx, route in enumerate(routes, 1):
            print('| {:>4} | {:<30} | {:<30} | {:>8} |'.format(
                    idx,
                    route.get('name_start', ''),
                    route.get('name_end', ''),
                    route.get('number', 0)
                    )
                    )
            print(line)
    else:
        print("Список работников пуст.")


def select(routes, command):
    '''
    Вывести выбранные маршруты
    '''
    parts = command.split(' ', maxsplit=1)
    station = parts[1]
    count = 0

    for route in routes:
        if (station == route["name_start"].lower() or
            station == route["name_end"].lower()):

            count += 1
            print('{:>4}: {}-{}, номер маршрута: {}'.format(count,
                  route["name_start"], route["name_end"], route["number"]))

    if count == 0:
        print("Маршрут не найден.")


def help():
    '''
    Вывести список команд
    '''
    print("Список команд:\n")
    print("add - добавить маршрут;")
    print("list - вывести список маршрутов;")
    print("select <пункт> - запросить информацию"+
          " о маршруте с указанным пунктом;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def main():
    '''
    Основная функция 
    '''
    routes = []

    while True:

        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            route = add()
            routes.append(route)

            if len(routes) > 1:
                routes.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            list(routes)

        elif command.startswith('select '):
            select(routes, command)

        elif command == 'help':
            help()
            
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
