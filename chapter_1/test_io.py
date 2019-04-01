#!/usr/bin/env python3

print('Type integers, each follow by Enter; or just Enter to finish')

total = 0
count = 0

while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:  # (EOF) end of file
        break
if count:
    print(f'count = {count}, total = {total}, mean = {total/count}')