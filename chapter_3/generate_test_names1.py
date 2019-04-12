#!/usr/bin/env python3

import random


def get_forenames_and_surnames():
    forenames = list()
    surnames = list()

    for names, filename in ((forenames, 'data/forenames.txt'),
                            (surnames, 'data/surnames.txt')):
        for name in open(filename, encoding='utf-8'):
            names.append(name.rstrip())
    return forenames, surnames


forenames, surnames = get_forenames_and_surnames()

fh = open('test_names1.txt', 'w', encoding='utf-8')
import time

start = time.monotonic()
for i in range(5000):
    fh.write(f'{random.choice(forenames)} {random.choice(surnames)}\n')
print(time.monotonic() - start)
