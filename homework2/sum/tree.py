import numpy as np


class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        # self.level = 0
        self.output = None


class Tree(object):
    """
    This class is a binary tree.
    """

    def __init__(self, root=None):
        """
        :param root: This must be a Node type
        """
        self.root = root

    def add_node(self, val, curNode):
        """
        Add a node at the current level
        :param val: the value of the node you want to add
        :param curNode: the place you want to add the node
        :param level: level of the tree
        :return:
        """
        if val < curNode.value:
            if curNode.left is None:
                curNode.left = Node(val)
                # curNode.left.level = level
            else:
                # level +=1
                self.add_node(val, curNode.left)
        else:
            if curNode.right is None:
                curNode.right = Node(val)
            else:
                self.add_node(val, curNode.right)

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.add_node(val, self.root)

    def print_all_elements(self, node):
        """
        This function is not the answer to the homework.
        It is just a quick way to print all elements
        :param node: start node
        :return:
        """
        if node is None:
            return
        else:
            print(node.value)

        self.print_all_elements(node.left)
        self.print_all_elements(node.right)

    def get_height(self, node):
        return 0 if not node else 1 + max(self.get_height(node.left),
                                          self.get_height(node.right))

    def print_tree(self, root):
        """
        This function is the answer to the homework.
        :return:
        """

        def update_output(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2

            self.output[row][mid] = str(node.value)
            update_output(node.left, row + 1, left, mid - 1)
            update_output(node.right, row + 1, mid + 1, right)

        height = self.get_height(self.root)
        width = 2 ** height - 1

        self.output = [[''] * width for i in range(height)]
        update_output(node=root, row=0, left=0, right=width - 1)

        print(np.asarray(self.output))
        return self.output


if __name__ == '__main__':
    a_tree = Tree()
    k = np.random.randint(0, 10, size=5)
    for i in k:
        a_tree.add(i)

    result = a_tree.print_tree(a_tree.root)
