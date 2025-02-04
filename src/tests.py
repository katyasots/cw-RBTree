from modules.RBTree import RBTree
from random import randint


def test_insert_random():
    data = [randint(0, 100) for _ in range(10000)]
    tree = RBTree()
    for i in data:
        tree.insertNode(i)
    assert tree.in_order(tree.root, []) == sorted(data)


def test_insert():
    tree = RBTree()
    for i in range(10):
        tree.insertNode(i)
    assert tree.in_order(tree.root, []) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert tree.root.val == 3
