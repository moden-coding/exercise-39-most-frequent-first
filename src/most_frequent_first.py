#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    pass


def main():
    a = np.array([[1, 0, 5],
                  [2, 0, 6],
                  [3, 1, 7],
                  [4, 0, 8]])
    print("Input:")
    print(a)
    print("Rows sorted by frequency of column 1's value (most frequent first):")
    print(most_frequent_first(a, 1))

if __name__ == "__main__":
    main()
