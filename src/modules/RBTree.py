class Node():
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1 #new Node is red node


class RBTree():
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def insertNode(self, key):
        node = Node(key)
        node.val = key
        node.parent = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1

        curNode = self.root
        parentNode = None

        #find position for insert new node
        while curNode != self.NULL:
            parentNode = curNode
            if node.val < curNode.val:
                curNode = curNode.left
            else:
                curNode = curNode.right

        node.parent = parentNode
        if parentNode == None:
            self.root = node
        elif node.val < parentNode.val:
            parentNode.left = node
        else:
            parentNode.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fixInsert(node)

    def fixInsert(self, inserted):
        while inserted.parent.color == 1:
            if inserted.parent == inserted.parent.parent.right:
                uncle = inserted.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    inserted.parent.color = 0
                    inserted.parent.parent.color = 1
                    inserted = inserted.parent.parent
                else:
                    if inserted == inserted.parent.left:
                        inserted = inserted.parent
                        self.rightRotate(inserted)
                    inserted.parent.color = 0
                    inserted.parent.parent.color = 1
                    self.leftRotate(inserted.parent.parent)
            else:
                uncle = inserted.parent.parent.right
                if uncle.color == 1:
                    uncle.color = 0
                    inserted.parent.color = 0
                    inserted.parent.parent.color = 1
                    inserted = inserted.parent.parent
                else:
                    if inserted == inserted.parent.right:
                        inserted = inserted.parent
                        self.leftRotate(inserted)
                    inserted.parent.color = 0
                    inserted.parent.parent.color = 1
                    self.rightRotate(inserted.parent.parent)
            if inserted == self.root:
                break
        self.root.color = 0

    def leftRotate(self, pivot):
        child = pivot.right
        pivot.right = child.left
        if child.left != self.NULL:
            child.left.parent = pivot

        child.parent = pivot.parent
        if pivot.parent == None:
            self.root = child
        elif pivot == pivot.parent.left:
            pivot.parent.left = child
        else:
            pivot.parent.right = child
        child.left = pivot
        pivot.parent = child

    def rightRotate(self, pivot):
        child = pivot.left
        pivot.left = child.right
        if child.right != self.NULL:
            child.right.parent = pivot

        child.parent = pivot.parent
        if pivot.parent == None:
            self.root = child
        elif pivot == pivot.parent.right:
            pivot.parent.right = child
        else:
            pivot.parent.left = child
        child.right = pivot
        pivot.parent = child

    def printTree(self, root, offset):
        if root:
            self.printTree(root.right, offset + 7)
            print(' ' * offset, end='')
            print(root.val, "R" if root.color == 1 else "B")
            self.printTree(root.left, offset + 7)

    def in_order(self, root, node_list):
        if root.val != 0 or root.left or root.right:
            self.in_order(root.left, node_list)
            node_list.append(root.val)
            self.in_order(root.right, node_list)

        return node_list
