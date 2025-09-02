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

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if not current:
            return None
        if current.value == value:
            return current
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, current, value):
        if not current:
            return None

        if value < current.value:
            current.left = self._delete(current.left, value)
        elif value > current.value:
            current.right = self._delete(current.right, value)
        else:
           
            if not current.left and not current.right:
                return None
            
            if not current.left:
                return current.right
            if not current.right:
                return current.left
            
            successor = self._min_value_node(current.right)
            current.value = successor.value
            current.right = self._delete(current.right, successor.value)

        return current

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

  
    def height(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    
    def depth(self, value):
        return self._depth(self.root, value, 0)

    def _depth(self, current, value, d):
        if not current:
            return -1
        if current.value == value:
            return d
        elif value < current.value:
            return self._depth(current.left, value, d + 1)
        else:
            return self._depth(current.right, value, d + 1)

    
    def visualize(self, filename="bst_tree"):
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
   
    valores = [55, 30, 80, 20, 45, 70, 90]
    bst = BinarySearchTree()
    for v in valores:
        bst.insert(v)

    bst.visualize("fixed_bst")
    print("Altura da árvore fixa: ", bst.height())
    print("Profundidade do nó 45: ", bst.depth(45))

    print("Busca pelo valor 70: ", "Encontrado" if bst.search(70) else "Não encontrado")

    bst.delete(30)
    bst.visualize("fixed_bst_after_delete")

    bst.insert(60)
    bst.visualize("fixed_bst_after_insert")

 
    numeros_random = random.sample(range(1, 200), 15)
    bst_rand = BinarySearchTree()
    for n in numeros_random:
        bst_rand.insert(n)

    bst_rand.visualize("random_bst")
    print("Números inseridos: ", numeros_random)
    print("Altura da árvore randômica:", bst_rand.height())
