#!/usr/bin/env python3
"""
Molecules Problem
"""
__author__ = "Molecule Team: Meaghan Crowell and Jake Johnson"


def parse_input(inpt):
    # reading and stripping input from .txt file right now for testing,
    # will convert to sysargs for final
    lines = [x.strip() for x in open(inpt).readlines()]
    # group lines in groups of 4
    return [lines[i:i+4]
            for i in range(0, len(lines[:-1]), 4)]


def main():
    datasets = parse_input('input.txt')
    print(datasets)


if __name__ == "__main__":
    main()
