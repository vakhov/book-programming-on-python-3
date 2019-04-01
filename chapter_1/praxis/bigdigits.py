#!/usr/bin/env python3

import sys

from my_digits import digits as md
try:
    digits = sys.argv[1]
    for row in range(7):  # кол-во строк в каждой большой цифре состоит из 7 строк
        line = ''
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = md[number]
            digit_row = digit[row].replace('*', str(number))  # заменяем в строке * на занчения этого числа
            line += f'{digit_row}  '
            column += 1
        print(line)
        row += 1
except IndexError:
    print('usage: ./bigdigits.py <number>')
except ValueError as err:
    print(f'{err} in {digits}')
