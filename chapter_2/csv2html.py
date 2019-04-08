#!/usr/bin/env python3
import sys


def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = 'lightgreen'
            elif count % 2:
                color = 'white'
            else:
                color = 'lightyellow'
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()


def print_start():
    print('<table border="1">')


def print_line(line, color, maxwidth):
    print('<tr bgcolor="{0}">'.format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(',', '')
            try:
                x = float(number)
                print('<td align="right">{0:d}</td>'.format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(' And ', ' and ')
                field = escape_html(field)
                if len(field) <= maxwidth:
                    print('<td>{0}</td>'.format(field))
                else:
                    print('<td>{0:.{1}} ...</td>'.format(field, maxwidth))
    print('</tr>')


def extract_fields(line):
    pass


def escape_html(field):
    pass


def print_end():
    print('</table>')


if __name__ == '__main__':
    main()