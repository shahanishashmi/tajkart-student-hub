import unittest

from _includes.solutions.array_total import array_total
from _includes.solutions.binary_search import binary_search
from _includes.solutions.count_vowels import count_vowels
from _includes.solutions.factorial import factorial
from _includes.solutions.first_duplicate import first_duplicate
from _includes.solutions.graph_reachable import graph_reachable
from _includes.solutions.insertion_sort import insertion_sort
from _includes.solutions.tree_height import tree_height


class SolutionTests(unittest.TestCase):
    def test_array_total(self):
        self.assertEqual(array_total([4, 2, 8]), 14)
        self.assertEqual(array_total([]), 0)

    def test_first_duplicate(self):
        self.assertEqual(first_duplicate([3, 1, 3, 1]), 3)
        self.assertIsNone(first_duplicate([2, 4, 6]))
        self.assertIsNone(first_duplicate([]))

    def test_binary_search_requires_sorted_values(self):
        self.assertEqual(binary_search([1, 4, 7, 9], 7), 2)
        self.assertEqual(binary_search([1, 4, 7, 9], 5), -1)
        self.assertEqual(binary_search([], 5), -1)

    def test_insertion_sort_does_not_change_input(self):
        values = [4, 1, 3, 1]
        self.assertEqual(insertion_sort(values), [1, 1, 3, 4])
        self.assertEqual(values, [4, 1, 3, 1])
        self.assertEqual(insertion_sort([]), [])

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Tajkart"), 2)
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels(""), 0)

    def test_tree_height(self):
        tree = ("a", ("b", None, None), ("c", None, ("d", None, None)))
        self.assertEqual(tree_height(tree), 3)
        self.assertEqual(tree_height(None), 0)

    def test_graph_reachability(self):
        graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
        self.assertTrue(graph_reachable(graph, "A", "D"))
        self.assertFalse(graph_reachable(graph, "C", "D"))
        self.assertFalse(graph_reachable(graph, "missing", "D"))


if __name__ == "__main__":
    unittest.main()
