#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print(f'usage: {sys.argv[0]} word infile1 [infile2 [... infileN]]')
    sys.exit()

word = sys.argv[1]
for filename in sys.argv[2:]:
    for lino, line in enumerate(open(filename), start=1):
        if word in line:
            print(f'{filename}:{lino}:{line.rstrip()[:40]}')
