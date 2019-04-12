#!/usr/bin/env python3

import string
import sys
import time

words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
star = time.monotonic()
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] = words.get(word, 0) + 1
stop = time.monotonic() - star

for word in sorted(words):
    # if words[word] > 1000:
    print("'{0}' occurs {1} times".format(word, words[word]))

print(stop)
