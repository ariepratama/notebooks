from graphviz import Digraph
from .core import LispTree

def draw_lisp_tree(root: LispTree):
    g = Digraph()

    edges = []
    exploration_stack = []
        
    exploration_stack.append(root)

    while len(exploration_stack) > 0:
        root = exploration_stack.pop(0)
        
        for child in root.children:
            edges.append((root.node_name, child.node_name))
            if len(child.children) > 0:
                exploration_stack.append(child)

    for edge in set(edges):
        g.edge(*edge)
    
    return g