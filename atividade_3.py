import random
from graphviz import Digraph

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left:
                self._insert(current.left, value)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert(current.right, value)
            else:
                current.right = Node(value)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        result = []
        if node.left:
            result.extend(self.inorder(node.left))
        result.append(node.value)
        if node.right:
            result.extend(self.inorder(node.right))
        return result

    def preorder(self, node=None):
        if node is None:
            node = self.root
        result = [node.value]
        if node.left:
            result.extend(self.preorder(node.left))
        if node.right:
            result.extend(self.preorder(node.right))
        return result

    def postorder(self, node=None):
        if node is None:
            node = self.root
        result = []
        if node.left:
            result.extend(self.postorder(node.left))
        if node.right:
            result.extend(self.postorder(node.right))
        result.append(node.value)
        return result

    def visualize(self, filename="bst_traversal"):
        dot = Digraph()

        def add_nodes_edges(node):
            if node:
                dot.node(str(id(node)), str(node.value))
                if node.left:
                    dot.edge(str(id(node)), str(id(node.left)))
                    add_nodes_edges(node.left)
                if node.right:
                    dot.edge(str(id(node)), str(id(node.right)))
                    add_nodes_edges(node.right)

        add_nodes_edges(self.root)
        dot.render(filename, format="png", cleanup=True)
        print(f"Árvore salva como {filename}.png")


if __name__ == "__main__":

    valores_fixos = [55, 30, 80, 20, 45, 70, 90]
    bst_fixa = BinarySearchTree()
    for v in valores_fixos:
        bst_fixa.insert(v)

    bst_fixa.visualize("fixed_traversal")
    print("Árvore fixa: ", valores_fixos)
    print("In-Order: ", bst_fixa.inorder())
    print("Pre-Order: ", bst_fixa.preorder())
    print("Post-Order: ", bst_fixa.postorder())
    print("-" * 40)

    valores_random = random.sample(range(1, 100), 10)
    bst_rand = BinarySearchTree()
    for v in valores_random:
        bst_rand.insert(v)

    bst_rand.visualize("random_traversal")
    print("Árvore randômica: ", valores_random)
    print("In-Order : ", bst_rand.inorder())
    print("Pre-Order: ", bst_rand.preorder())
    print("Post-Order: ", bst_rand.postorder())
