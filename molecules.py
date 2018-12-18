#!/usr/bin/env python2
"""
Molecules Problem
"""
from itertools import permutations

__author__ = "Molecule Team: Meaghan Crowell and Jake Johnson"


def parse_input(inpt):
    """take input strings and compile them into a
    list with dataset groups of 4"""

    # reading and stripping input from .txt file right now for testing,
    # will convert to sysargs for final
    with open(inpt) as f:
        lines = [x.strip() for x in f.readlines()]
    # group lines in lists of len 4
    return [lines[i:i+4]
            for i in range(0, len(lines[:-1]), 4)]


def find_intersections(w1, w2, edges):
    """
  # Return a sorted list of tuples that represent intersection points.
  # The sorting order should be from best to worst (e.g. lowest indices
  # to highest) Return None if no intersections are found.
    """
    intersections = []

    for i, x in enumerate(w1):
        for j, y in enumerate(w2):
            if x == y:
                intersections.append((i, j))
    intersections = [(x, y)
                     for x, y in intersections if x not in edges
                     and y not in edges and x-10 != 0 and y-10 != 0]
    intersections.sort(key=lambda x: sum(x))
    return intersections if intersections else None


def find_largest_rect(intersections):
    res = []
    print(intersections)
    for x, y in intersections:
        res.append((10-x, 10-y))
    return res


def main():
    datasets = parse_input('input.txt')
    # perm_tuple = [x for x in permutations(datasets[0])]

    intersections = find_intersections(datasets[0][0], datasets[0][1], [0, 11])
    rectangles = find_largest_rect(intersections)
    print(rectangles)


if __name__ == "__main__":
    main()
