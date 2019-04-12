#!/usr/bin/env python3

import string
import sys
import time
import collections

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
star = time.monotonic()
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1
stop = time.monotonic() - star


def by_value(item):
    return item[1]


for word, count in sorted(words.items(), key=by_value):
    # if words[word] > 1000:
    print("'{0}' occurs {1} times".format(word, count))

print(stop)
