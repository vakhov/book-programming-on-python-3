#!/usr/bin/env python3

import random

articles = ['the', 'a', 'another', 'her', 'his']  # артикль
subjects = ['cat', 'dog', 'horse', 'man', 'woman', 'boy', 'girl']  # существительное
verbs = ['sang', 'ran', 'jumped', 'said', 'fought', 'swam', 'saw', 'heard', 'felt', 'slept', 'hopped', 'hoped', 'cried',
         'laughed', 'walked']  # глагол
adverbs = ['loudly', 'quietly', 'quickly', 'slowly', 'well', 'badly', 'rudely', 'politely']  # наречие

structures = [[articles, subjects, verbs, adverbs], [articles, subjects, verbs]]

for _ in range(5):
    line = ''
    for structure in structures[random.randint(0, 1)]:
        line += f'{random.choice(structure)} '
    print(line)
