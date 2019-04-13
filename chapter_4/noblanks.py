#!/usr/bin/env python3

"""
Удаление пустых строк в файлах
"""
import os
import sys


def read_data(file_name):
    _lines = []
    fh = None
    try:
        fh = open(file_name, encoding="utf8")
        for line in fh:
            if line.strip():
                _lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
    return _lines


def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, 'w', encoding='utf-8')
        for line in lines:
            fh.write(line)
    except EnvironmentError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print(f'usage: {sys.argv[0]} file1 [file2 [... fileN]]')
        sys.exit()

    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, f'{os.path.splitext(filename)[0]}.nb')
