""" Created by Jieyi on 2/11/16. """
from __interface__ import BinaryTreeNode


class BinaryTree:
    def __init__(self):
        self.__head = None

    def add_node(self, obj):
        if self.__head is None:
            self.__head = BinaryTreeNode(obj)
            return

        th = self.__head
        while True:
            if obj > th.data:
                if th.right is not None:
                    th = th.right
                else:
                    th.right = BinaryTreeNode(obj)
                    return
            elif obj < th.data:
                if th.left is not None:
                    th = th.left
                else:
                    th.left = BinaryTreeNode(obj)
                    return

    def show(self):
        self._in_order(self.__head)

    def _in_order(self, node):
        if node is not None:
            self._in_order(node.left)
            print(node.data)
            self._in_order(node.right)

    @property
    def get_head(self):
        return self.__head


def main():
    bt = BinaryTree()
    bt.add_node(1)
    bt.add_node(3)
    bt.add_node(0)
    bt.add_node(4)

    bt.show()


if __name__ == '__main__':
    main()
