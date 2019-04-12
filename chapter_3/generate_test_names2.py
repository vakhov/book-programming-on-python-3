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

fh = open('test_names2.txt', 'w', encoding='utf-8')

limit = 100
years = list(range(1970, 2013)) * 3
for year, forename, surname in zip(
        random.sample(years, limit),
        random.sample(forenames, limit),
        random.sample(surnames, limit)):
    name = f'{forename} {surname}'
    fh.write('{0:.<25}.{1}\n'.format(name, year))
