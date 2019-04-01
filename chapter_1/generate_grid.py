#!/usr/bin/env python3
"""
Генерация числовых рядов
"""
import random


def get_int(msg, minimum, default=None):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print(f'must be >= {minimum}')
            else:
                return i
        except IndexError as err:
            print(err)


rows = get_int('rows: ', 1)
columns = get_int('columns: ', 1)
minimum = get_int('minimum (or Enter for 0): ', -1_000_000, 0)

default = 1_000
if default < minimum:
    default = 2 * default
maximum = get_int(f'maximum (or Enter for {default}): ', minimum, default)

row = 0

while row < rows:
    line = ''
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10:
            s = f' {s}'
        line += s
        column += 1
    print(line)
    row += 1
