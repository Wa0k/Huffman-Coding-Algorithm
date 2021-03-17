#!/usr/bin/env python
# -*- coding: Utf-8 -*-

"""
    Huffman algorithm:
    ==================

    This script allows to compress the text into the text.txt file according to
    the Huffman's algorithm, and save the output (i.e. the compressed text) into
    the output.txt file.
"""

__author__ = "ONILLON Louis"
__copyright__ = "Copyright (c) 2021 Wa0k, Huffman algorithm"
__license__ = "MIT License"
__version__ = "1.0.0"
__contact__ = "wa0k@mailo.com"
__date__ = "23/02/2021"
__status__ = "Production"
__username__ = "W@0k"


class HuffmanTree:
    def __init__(self, letter, nb_occ, left=None, right=None):
        self.letter = letter
        self.nb_occ = nb_occ
        self.left = left
        self.right = right

    def __lt__(self, tree2) -> bool:
        """ Compares if the tree A is strictly superior to the tree B or not.

        A tree A is strictly superior to a tree B if the number of occurrences
        indicated in A is strictly superior to the number of occurrences of B.

        :param tree2: the secondly Huffman tree to compare
        :type tree2: HuffmanTree
        :return: a boolean value that indicates if the tree A is strictly
        superior to the tree B
        """
        return self.nb_occ > tree2.nb_occ

    def is_leaf(self) -> bool:
        """ Indicates if the tree is a leaf or not.
        A tree is a leaf if and only if his left and right subtree are empty.

        :return: a boolean value that indicates if the tree is a leaf or not
        """
        return self.left is None and self.right is None


def build_tree_list(text: str) -> list:
    """ Makes a list of Huffman trees, each reduced to a leaf.

    :param text: the text to be coded
    :return: a list of Huffman trees
    """
    dict_occ = count_occurrences(text)
    trees_list = list()
    for letter, occ, in dict_occ.items():
        trees_list.append(HuffmanTree(letter, occ))
    return trees_list


def count_occurrences(text: str) -> dict:
    """ Counts the number of time that each different character appears in the
    text.

    :param text: the text to be coded
    :return: a dictionary with each character of the text as a key and the
    number of appearance of this character in the text in value
    """
    occ = dict()
    for char in text:
        if char not in occ:
            occ[char] = 0
        occ[char] = occ[char] + 1
    return occ


def merge_tree(left_subtree: HuffmanTree, right_subtree: HuffmanTree) -> HuffmanTree:
    """ Merges two Huffman trees into one.

    The root of the new Huffman tree is equal to the sum of the number of
    occurrences of its two subtrees.

    :param left_subtree: an Huffman tree with the character that has the most
    occurrences
    :param right_subtree: an Huffman tree with the character that has the least
    occurrences
    :return: a new Huffman tree based on both trees in parameter
    """
    total_occ = left_subtree.nb_occ + right_subtree.nb_occ
    return HuffmanTree(None, total_occ, left_subtree, right_subtree)


def path(tree: HuffmanTree, current_path: str, code: dict) -> dict:
    """ Browses through the entire Huffman tree to get the code of each characters
    of our text.

    :param tree: the tree that is being browsed
    :param current_path: the current path that is being browsed
    :param code: the dictionary containing the characters code
    :return: the entire dictionary with all characters code of the text.
    """
    if tree is None:
        return None
    elif tree.is_leaf():
        code[tree.letter] = current_path
    else:
        path(tree.left, current_path + "0", code)
        path(tree.right, current_path + "1", code)
    return code


if __name__ == "__main__":
    import bisect
    with open("text.txt", mode="r", encoding="utf-8") as data:
        text = " ".join([line.strip("\n") for line in data.readlines()])

    trees_list = build_tree_list(text)
    # We sort the trees_list according to the the number of occurrences in descending order.
    trees_list.sort()
    while len(trees_list) > 1:
        right_tree = trees_list.pop()
        left_tree = trees_list.pop()
        new_tree = merge_tree(left_tree, right_tree)
        bisect.insort(trees_list, new_tree)
    # The last tree of our trees_list is the Huffman tree.
    huffman_tree = trees_list.pop()
    # We browses through the tree to find the codes.
    codes = path(huffman_tree, "", {})

    with open("output.txt", mode="w", encoding="utf-8") as output:
        for char, code in codes.items():
            output.write(char + " -> " + code + "\n")
