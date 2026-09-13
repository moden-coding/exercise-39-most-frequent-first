#!/usr/bin/env python3
"""Tests for the Most Frequent First assignment."""

import unittest
from collections import defaultdict

import numpy as np

from src.most_frequent_first import most_frequent_first


def sort_rows(a):
    """Sort rows in lexicographical order."""
    n, m = a.shape
    keys = np.arange(m - 1, -1, -1)  # columns from last to first
    return a[np.lexsort(a.T[keys])]


class TestMostFrequentFirst(unittest.TestCase):
    """most_frequent_first(a, c) -> rows of a sorted by frequency in column c."""

    def test_same_rows(self):
        n, m = 10, 10
        a = np.random.randint(0, 10, (n, m))
        for c in range(m):
            result = most_frequent_first(a, c)
            np.testing.assert_allclose(
                sort_rows(a),
                sort_rows(result),
                err_msg="The result does not contain the same rows as the "
                "input for column %i and array %s" % (c, a),
            )

    def test_content(self):
        n, m = 10, 10
        for c in range(m):
            a = np.random.randint(0, 10, (n, m))
            result = most_frequent_first(a, c)
            multiplicities = defaultdict(int)
            b = a[:, c]
            for x in b:
                multiplicities[x] += 1
            previous_multiplicity = np.inf
            for x in result[:, c]:
                self.assertGreaterEqual(
                    previous_multiplicity,
                    multiplicities[x],
                    msg="Result\n%s not correctly sorted according to "
                    "column %i! Rows must appear in decreasing order of "
                    "how often their value in column %i occurs."
                    % (result, c, c),
                )
                previous_multiplicity = multiplicities[x]


if __name__ == "__main__":
    unittest.main()
