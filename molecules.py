#!/usr/bin/env python2
"""
Molecules Problem
"""
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


def main():
    datasets = parse_input('input.txt')
    print(datasets)


if __name__ == "__main__":
    main()
