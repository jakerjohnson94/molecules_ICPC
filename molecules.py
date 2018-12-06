#!/usr/bin/env python3
"""
Module Docstring
"""
from helper.functions import strip_list


__author__ = "Molecule Team: Meaghan Crowell and Jake Johnson"


def parse_input(inpt):
    # reading input from .txt file right now for testing, will convert to sysargs for final
    lines = open(inpt).readlines()

    # group lines in groups of 4 and remove newline chars
    datasets = [strip_list(lines[i:i+4])
                for i in range(0, len(lines[:-1]), 4)]

    return datasets


def main():
    datasets = parse_input('input.txt')
    print(datasets)


if __name__ == "__main__":
    main()
