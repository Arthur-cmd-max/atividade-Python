import random
from graphviz import Digraph

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def visualize_tree(node, filename="tree"):
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
    
    add_nodes_edges(node)
    dot.render(filename, format="png", cleanup=True)
    print(f"Árvore salva como {filename}.png")

def build_fixed_tree():

    left = Node("*", Node("+", Node(7), Node(3)), Node("-", Node(5), Node(2)))
    right = Node("*", Node(10), Node(20))
    root = Node("/", left, right)
    return root

def generate_random_expression(depth=2):
    operators = ["+", "-", "*", "/"]
    if depth == 0:
        return str(random.randint(1, 9))
    left = generate_random_expression(depth - 1)
    right = generate_random_expression(depth - 1)
    op = random.choice(operators)
    return f"({left} {op} {right})"

def build_tree_from_expression(expr):
    tokens = expr.replace("(", " ( ").replace(")", " ) ").split()

    def parse(tokens):
        token = tokens.pop(0)
        if token == "(":
            left = parse(tokens)
            op = tokens.pop(0)
            right = parse(tokens)
            tokens.pop(0)  
            return Node(op, left, right)
        else:
            return Node(token)

    return parse(tokens)

if __name__ == "__main__":
    fixed_tree = build_fixed_tree()
    visualize_tree(fixed_tree, "fixed_tree")

    random_expr = generate_random_expression(depth=2)
    print("Expressão Randômica Gerada:", random_expr)
    random_tree = build_tree_from_expression(random_expr.split())
    visualize_tree(random_tree, "random_tree")
