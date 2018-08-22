import unittest
from sum.tree import Tree


class TestClass(unittest.TestCase):

    def test_1(self):
        """
        This function tests the case where the root is None
        :return:
        """
        a_tree = Tree()
        result = a_tree.print_tree(a_tree.root)
        assert result == []

    def test_2(self):
        """
        This function tests the case where the there is only 1 side
        :return:
        """
        a_tree = Tree()
        a_tree.add(4)
        a_tree.add(3)
        a_tree.add(2)
        a_tree.add(1)

        result = a_tree.print_tree(a_tree.root)
        assert result == [
            ['', '', '', '', '', '', '', '4', '', '', '', '', '', '', ''],
            ['', '', '', '3', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '2', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['1', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]

    def test_3(self):
        """
        This function tests the case of a balanced tree
        :return:
        """
        a_tree = Tree()
        a_tree.add(1)
        a_tree.add(0)
        a_tree.add(2)

        result = a_tree.print_tree(a_tree.root)
        assert result == [['', '1', ''],
                          ['0', '', '2']]

    def test_4(self):
        """
        This function tests the case of a unbalanced tree
        :return:
        """
        a_tree = Tree()
        a_tree.add(2)
        a_tree.add(7)
        a_tree.add(0)
        a_tree.add(4)
        a_tree.add(9)
        a_tree.add(6)

        result = a_tree.print_tree(a_tree.root)
        assert result == [
            ['', '', '', '', '', '', '', '2', '', '', '', '', '', '', ''],
            ['', '', '', '0', '', '', '', '', '', '', '', '7', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '4', '', '', '', '9', ''],
            ['', '', '', '', '', '', '', '', '', '', '6', '', '', '', '']]
