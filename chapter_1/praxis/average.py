#!/usr/bin/env python3


numbers = []
total = 0
lowest = None
highest = None
while True:
    try:
        list_ = []
        line = input('enter number or Enter to finish: ')
        if not line:
            break
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

if numbers:
    print(numbers)
    print(f'count = {len(numbers)}, sum = {total}, lowest = {lowest}, highest = {highest}, mean = {total/len(numbers)}')
