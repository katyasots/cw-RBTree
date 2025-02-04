from modules.RBTree import RBTree
from random import randint


if __name__ == "__main__":
    random_numbers = [randint(0, 100) for _ in range(int(input('AMOUNT OF ELEMENTS (>2): ')))]
    tree = RBTree()
    for i in random_numbers:
        tree.insertNode(i)
    print(f'START TREE:\n{"-" * 100}')
    tree.printTree(tree.root, 0)
    num_to_insert = randint(0, 100)
    print(f'{"-" * 100}\nAFTER INSERT {num_to_insert}:\n{"-" * 100}')
    tree.insertNode(num_to_insert)
    tree.printTree(tree.root, 0)
