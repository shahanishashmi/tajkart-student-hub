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

    def test_array_total_handles_zero_and_negative_values(self):
        self.assertEqual(array_total([-3, 3]), 0)
        self.assertEqual(array_total([0, -4, 2]), -2)

    def test_first_duplicate(self):
        self.assertEqual(first_duplicate([3, 1, 3, 1]), 3)
        self.assertIsNone(first_duplicate([2, 4, 6]))
        self.assertIsNone(first_duplicate([]))

    def test_first_duplicate_handles_adjacent_and_string_values(self):
        self.assertEqual(first_duplicate(["a", "a", "b"]), "a")
        self.assertEqual(first_duplicate(["x", "y", "z", "y"]), "y")

    def test_binary_search_requires_sorted_values(self):
        self.assertEqual(binary_search([1, 4, 7, 9], 7), 2)
        self.assertEqual(binary_search([1, 4, 7, 9], 5), -1)
        self.assertEqual(binary_search([], 5), -1)

    def test_binary_search_handles_boundaries_and_single_item(self):
        self.assertEqual(binary_search([1, 4, 7, 9], 1), 0)
        self.assertEqual(binary_search([1, 4, 7, 9], 9), 3)
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 4), -1)

    def test_insertion_sort_does_not_change_input(self):
        values = [4, 1, 3, 1]
        self.assertEqual(insertion_sort(values), [1, 1, 3, 4])
        self.assertEqual(values, [4, 1, 3, 1])
        self.assertEqual(insertion_sort([]), [])

    def test_insertion_sort_handles_single_sorted_and_reverse_inputs(self):
        for values in ([5], [1, 2, 3], [3, 2, 1]):
            with self.subTest(values=values):
                original = list(values)
                self.assertEqual(insertion_sort(values), sorted(values))
                self.assertEqual(list(values), original)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(12), 479001600)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Tajkart"), 2)
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_is_case_insensitive_and_limited_to_english_vowels(self):
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("áéíóú"), 0)

    def test_tree_height(self):
        tree = ("a", ("b", None, None), ("c", None, ("d", None, None)))
        self.assertEqual(tree_height(tree), 3)
        self.assertEqual(tree_height(None), 0)

    def test_tree_height_handles_a_leaf_and_left_only_branch(self):
        self.assertEqual(tree_height(("root", None, None)), 1)
        self.assertEqual(tree_height(("a", ("b", ("c", None, None), None), None)), 3)

    def test_graph_reachability(self):
        graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
        self.assertTrue(graph_reachable(graph, "A", "D"))
        self.assertFalse(graph_reachable(graph, "C", "D"))
        self.assertFalse(graph_reachable(graph, "missing", "D"))

    def test_graph_reachability_terminates_on_cycles_and_accepts_same_endpoint(self):
        graph = {"A": ["B"], "B": ["C"], "C": ["A"], "D": []}
        self.assertTrue(graph_reachable(graph, "A", "A"))
        self.assertFalse(graph_reachable(graph, "A", "D"))
        self.assertTrue(graph_reachable(graph, "D", "D"))


if __name__ == "__main__":
    unittest.main()
