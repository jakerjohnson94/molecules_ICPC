#!/usr/bin/env python2
"""
Molecules Problem
"""
# from itertools import permutations
import itertools
__author__ = "Molecule Team: Meaghan Crowell and Jake Johnson"


# def parse_input(inpt):
#     """take input strings and compile them into a
#     list with dataset groups of 4"""
#     # reading and stripping input from .txt file right now for testing,
#     # will convert to sysargs for final
#     with open(inpt) as f:
#         lines = [x.strip() for x in f.readlines()]
#     # group lines in lists of len 4
#     return [lines[i:i+4]
#             for i in range(0, len(lines[:-1]), 4)]

def rectangle_tuples(x):
    num_range = range(1, int(x + 1))
    pairs = list(itertools.combinations_with_replacement(num_range, 2))
    pairs.reverse()

    # Sort from largest rectangle area to smallest rectangle area
    pairs.sort(key=lambda x: x[0] * x[1], reverse=True)
    return pairs


# def find_intersections(w1, w2, edges):
#     """
#   # Return a sorted list of tuples that represent intersection points.
#   # The sorting order should be from best to worst (e.g. lowest indices
#   # to highest) Return None if no intersections are found.
#     """
#     intersections = []

#     for i, x in enumerate(w1):
#         for j, y in enumerate(w2):
#             if x == y:
#                 intersections.append((i, j))

#     intersections = [(x, y)
#                      for x, y in intersections if x not in edges
#                      and y not in edges and x-10 != 0 and y-10 != 0]

#     intersections.sort(key=lambda x: sum(x))

#     return intersections if intersections else None


# def find_largest_rect(length):
#     length = length - 2
#     res = []
#     for i in range(2, length):
#         for j in range(2, i+1):
#             res.append((i, j))
#     return sorted(res, key=lambda x: x[0] * x[1], reverse=True)


def best_fit(w, h, across1, across2, down1, down2):
    """Tries to fit a rectangle into a set of 4 molecule strings, 
    returns true if found"""
    # across and down
    for a1 in range(1, 12 - w):
        for d1 in range(1, 12 - h):
            if across1[a1] != down1[d1]:
                continue
            # if it comes past this continue,
            # we might have a rectangle that works
            for a2 in range(1, 12 - w):
                if across2[a2] != down1[d1 + h]:
                    continue
                for d2 in range(1, 12 - h):
                    if across1[a1+w] != down2[d2]:
                        continue
                    if across2[a2+w] != down2[d2+h]:
                        continue
                    return True

    return False


def main():
    vals = ['CDBADCBBEFEF', 'DACCBADAFEAB', 'EFBDCAADBDCD', 'ABCDABCDABCD']

    perms = itertools.permutations(vals)
    rectangles = rectangle_tuples(12)
    res = []
    for across1, across2, down1, down2 in perms:
        for w, h in rectangles:
            if best_fit(w, h, across1, across2, down1, down2):
                res.append(
                    (w, h, best_fit(w, h, across1, across2, down1, down2)))

    res = sorted(res, key=lambda x: x[0] * x[1],
                 reverse=True)

    print(res)
    # datasets = parse_input('input.txt')
    # perm_tuple = [x for x in permutations(datasets[0])]
    # string_length = len(datasets[0][0])
    # intersections = find_intersections(
    #     datasets[0][0], datasets[0][1], [0, 11])

    # rectangles = find_largest_rect(string_length)

    # print('rectangles', rectangles)
    # print('intersections', intersections)
    # print(rectangles)


if __name__ == "__main__":
    main()
