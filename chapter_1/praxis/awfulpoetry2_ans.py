#!/usr/bin/env python3

import random
import sys


articles = ['the', 'a', 'another', 'her', 'his']  # артикль
subjects = ['cat', 'dog', 'horse', 'man', 'woman', 'boy', 'girl']  # существительное
verbs = ['sang', 'ran', 'jumped', 'said', 'fought', 'swam', 'saw', 'heard', 'felt', 'slept', 'hopped', 'hoped', 'cried',
         'laughed', 'walked']  # глагол
adverbs = ['loudly', 'quietly', 'quickly', 'slowly', 'well', 'badly', 'rudely', 'politely']  # наречие

structures = [[articles, subjects, verbs, adverbs], [articles, subjects, verbs]]

lines = 5
if len(sys.argv) > 1:
    try:
        number = int(sys.argv[1])
        if 1 <= lines <= 10:
            line = number
        else:
            print("lines must be 1-10 inclusive")
    except ValueError:
        print("usage: badpoetry.py [lines]")

for _ in range(lines):
    line = ''
    for structure in structures[random.randint(0, 1)]:
        line += f'{random.choice(structure)} '
    print(line)
