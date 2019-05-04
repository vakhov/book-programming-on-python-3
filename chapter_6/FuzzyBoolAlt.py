#!/usr/bin/env python3


class FuzzyBool(float):
    # def __new__(cls, value=0.0):
    #     return super().__new__(cls, value if 0.0 <= value <= 1.0 else 0.0)

    def __int__(self, value=0.0):
        return super(FuzzyBool, self).__int__(value if 0.0 <= value <= 1.0 else 0.0)


def conjunction(*fuzzies):
    return FuzzyBool(min(fuzzies))


def disjunction(*fuzzies):
    return FuzzyBool(max(fuzzies))
