#!/usr/bin/env python3
# Copyright (c) 2019 Alexander Vakhov. All right reserved
r"""
Этот модуль представляет несколько функций манипулирования строками.
>>> is_balanced('(Python (is (not (lisp))))')
True
>>> shorten('The Crossing', 10)
'The Cro...'
>>> simplify(' some text with spurious whitespase ')
'some text with spurious whitespase'
"""

import string

__all__ = ['is_balanced', 'shorten', 'simplify']


def is_balanced(text: str, brackets: str = "()[]{}<>") -> str:
    r"""Возвращает True, если кол-во открывающихся ковычек,
        равно кол-ву закрывающихся, иначе False.

    >>> is_balanced('(Python (is (not (lisp))))')
    True
    >>> is_balanced('Python (is (not (lisp))))')
    False

    :param text: Проверяемая строка
    :param brackets: Необязательный параметр, строка с ковычками
    :return:
    """
    counts = {}
    left_for_right = {}
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left] = 0
        left_for_right[right] = left
    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_for_right:
            left = left_for_right[c]
            if counts[left] == 0:
                return False
            counts[left] -= 1
    return not any(counts.values())


def shorten(text: str, length: int = 25, indicator: str = "...") -> str:
    r""" Возвращает text или усеченную его копию с добавлением
        indicator в конце

    >>> shorten("Text")
    'Text'
    >>> shorten("Some text", 7)
    'Some...'
    >>> shorten("Some text", 7, '&')
    'Some t&'

    :param text: str Любой текст
    :param length: int максимальная длина строки string (включая indicator)
    :param indicator: str строка, добавляемая в конец результата, что бы показать,
                      что текст аргумента text был усечён
    :return: str text
    """
    if len(text) > length:
        text = f'{text[:length - len(indicator)]}{indicator}'
    return text


def simplify(text: str, whitespace: str = string.whitespace, delete: str = '') -> str:
    r""" Возвращает текст, из которго удалены лишние пробелы.

    Параметр whitespace - это строка символов, каждый из которых
    считается символом пробела. Если параметр delete не пустой,
    он должен содержать строку, и тогда все символы, входящие
    в состав строки delete, будут удалены из строки результата.

    >>> simplify(" this and\n that\t too")
    'this and that too'
    >>> simplify(" Washington D.C.\n")
    'Washington D.C.'
    >>> simplify(" Washington D.C.\n", delete=",;:.")
    'Washington DC'
    >>> simplify(" disemvoweled", delete="aeiou")
    'dsmvwld'

    :param text: Строка
    :param whitespace: Пробельные символы
    :param delete: Символы для удаления в text
    :return: str
    """
    result = []
    word = ''
    for char in text:
        if char in delete:
            continue
        elif char in whitespace:
            if word:
                result.append(word)
                word = ''
        else:
            word += char
    if word:
        result.append(word)
    return ' '.join(result)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
