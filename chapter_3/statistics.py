#!/usr/bin/env python3

import collections
import sys
import math

Statistics = collections.namedtuple('Statistics', 'mean mode median std_dev')


def caclulate_mode(frequencies, maximum_modes):
    highest_frequency = max(frequencies.values())
    mode = [number for number, frequency in frequencies.items()
            if math.fabs(frequency - highest_frequency) <=
            sys.float_info.epsilon]
    if not (1 <= len(mode) <= maximum_modes):
        mode = None
    else:
        mode.sort()
    return mode


def calculate_median(numbers):
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    median = numbers[middle]
    if len(numbers) % 2 == 0:
        median = (median + numbers[median - 1]) / 2
    return median


def calculate_std_dev(numbers, mean):
    total = 0
    for number in numbers:
        total += ((number - mean) ** 2)
    variance = total / (len(numbers) - 1)
    return math.sqrt(variance)


def read_data(filename, numbers, frequencies):
    for lino, line in enumerate(open(filename, encoding='ascii')):
        for x in line.split():
            try:
                number = float(x)
                numbers.append(number)
                frequencies[number] += 1
            except ValueError as err:
                print('{0}:{1} skipping {2}: {3}'.format(filename, lino, x, err))


def calculate_statistics(numbers, frequencies):
    mean = sum(numbers) / len(numbers)
    mode = caclulate_mode(frequencies, 3)
    median = calculate_median(numbers)
    std_dev = calculate_std_dev(numbers, mean)
    return Statistics(mean, mode, median, std_dev)


def print_results(count, statistics):
    real = '9.2f'

    if statistics.mode is None:
        modeline = ''
    elif len(statistics.mode) == 1:
        modeline = "mode = {0:{fmt}}\n".format(statistics.mode[0], fmt=real)
    else:
        modeline = ("mode = ["
                    ", ".join(["{0:.2f}".format(m) for m in statistics.mode] + "]\n"))
    print("""
    count = {0:6}
    mean = {1.mean:{fmt}}
    median = {1.median:{fmt}}
    {2} \
    std. dev. = {1.std_dev:{fmt}}
    """.format(count, statistics, modeline, fmt=real))


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print('usage: {0} file1 [file2 [... fileN]]'.format(sys.argv[0]))
        sys.exit()
    numbers = []
    frequencies = collections.defaultdict(int)
    for filename in sys.argv[1:]:
        read_data(filename, numbers, frequencies)
    if numbers:
        statistics = calculate_statistics(numbers, frequencies)
        print_results(len(numbers), statistics)
    else:
        print('no number found')


if __name__ == '__main__':
    main()
