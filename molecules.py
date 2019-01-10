#!/usr/bin/env python2
"""
Molecules Problem
"""
# from itertools import permutations
import itertools
import os
__author__ = "Jake J, Taylor G, Morgan"

default_input_vals = ['CDBADCBBEFEF',
                      'DACCBADAFEAB',
                      'EFBDCAADBDCD',
                      'ABCDABCDABCD',
                      'DACCBADAFEAB',
                      'EFBDCAADBDCD',
                      'ABCDABCDABCD',
                      'CDBADCBBEFEF',
                      'ABABABABABAB',
                      'CDCDCDCDCDCD',
                      'EEEEEEEEEEEE',
                      'FFFFFFFFFFFF',
                      'ABAAAAAAAABA',
                      'CBCCCCCCCCBC',
                      'DBDDDDDDDDBD',
                      'EBEEEEEEEEBE',
                      'ABBBBBBBBBBA',
                      'ACCCCCCCCCCA',
                      'ADDDDDDDDDDA',
                      'AEEEEEEEEEEA',
                      'BBBABBBABBBB',
                      'CCACCCACCCCC',
                      'DDDDADDADDDD',
                      'EEAEEAEEEEEE',
                      'Q']


def read_file(file):
    print(file)
    with open(file) as f:
        lines = [line for line in f.readlines()
                 if 'Q' not in line]
    return(lines)


def parse_input(lines):
    """take input strings and compile them into a
    list with dataset groups of 4"""

    # group lines in lists of len 4
    return [lines[i:i+4]
            for i in range(0, len(lines[:-1]), 4)]


def best_fit(w, h, across1, across2, down1, down2):
    """Tries to fit a rectangle into a set of 4 molecule strings,
    returns true if found"""
    # across and down
    for a1 in range(1, 12 - w):
        for d1 in range(1, 12 - h):
            if across1[a1] != down1[d1]:
                continue
            for a2 in range(1, 12 - w):
                if across2[a2] != down1[d1 + h - 1]:
                    continue
                for d2 in range(1, 12 - h):
                    if down2[d2] != across1[a1 + w - 1]:
                        continue
                    if down2[d2+h - 1] != across2[a2 + w - 1]:
                        continue

                    return True

    return False


def possible_rectangles(string_length):
    height = string_length - 1
    pairs = [(w, h)for w in range(2, height) for h in range(w, height)]
    # sort from biggest area to smallest
    pairs.sort(key=lambda x: x[0] * x[1], reverse=True)
    return pairs


def largest_area(dataset):
    pairs = possible_rectangles(12)
    perms = itertools.permutations(dataset)
    fits = []
    for across1, across2, down1, down2 in perms:
        for w, h in pairs:
            if best_fit(w, h, across1, across2, down1, down2):
                fits.append((w-2) * (h-2))

    largest_area = sorted(fits, reverse=True)[0] if fits else 0
    return largest_area


def main(inpt):
    vals = parse_input(inpt)

    for grp in vals:
        print(largest_area(grp))


if __name__ == "__main__":
    print(os.listdir('.'))
    if 'sample_input.txt' in os.listdir('.'):
        input_vals = read_file('sample_input.txt')
    else:
        input_vals = default_input_vals
    print(input_vals)
    main(input_vals)
