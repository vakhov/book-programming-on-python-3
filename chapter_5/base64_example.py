#!/usr/bin/env python3

import base64
import os

left_align_png = os.path.join(os.path.dirname(__file__),
                              "data/left_align.png")
binary = open(left_align_png, "rb").read()
ascii_text = ''
for i, c in enumerate(base64.b64encode(binary)):
    if i % 68 == 0:
        ascii_text += '\\\n'
    ascii_text += chr(c)

LEFT_ALIGN_PNG = b"""\
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABGdBTUEAALGPC/xhBQAA\
AAlwSFlzAAALEgAACxIB0t1+/AAAAUBJREFUeJztlrFKw0AYx38RhzyCY/oUqVskm5tE\
cBQEFynkEcQXKBS6SKDg2KG46ChmbJ7CjL5BXKQd7gvlzgRbm3An+ofj7rsj933587/7\
n8ciBICkUL0Z94Qw8gE46DXLFvDMichfaHH+kXSb0WDYKQZWNnI7xcB2uBNN3OpaidMR\
AC+TqRZ/3p8AUA1fASjyqfadfQYCGZT9a6CRbesMHIbXVwCU2cwDCGSh3HNjUxM1LiTf\
PJsBDjDgpTKY7K+BnU7UH/YCAw4wsHGnfy/4GVpeUL/HC4byB8v+NeCoFyzjUxkWjRWG\
0ZFazd9lpr4nurkfrDNg7U0YpyM37oGvOE5UE1xK+x6+tN1gnYEuNKCdnsG56t+e5LQY\
bmquu8PAmVT2+CwVV6rCyA9UfFMCkI+bN6p18tCWqcUzrDOwBh2zVCR+JZVeAAAAAElF\
TkSuQmCC"""

assert (bytes(ascii_text.replace("\\\n", ""), encoding="ascii") ==
        LEFT_ALIGN_PNG)

binary = base64.b64decode(LEFT_ALIGN_PNG)
open(left_align_png, "wb").write(binary)
print("saved", left_align_png)
