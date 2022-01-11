from typing import Text

class LispTree:
    def __init__(self, node_name: Text, depth: int = -1):
        self.node_name = node_name
        self.depth = depth
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    
    def __str__(self):
        children_str = ""

        if len(self.children) > 0:
            children_str = [str(child) for child in self.children]

        return "LispTree ({},{}){}".format(self.node_name, self.depth, children_str, )

    def __repr__(self):
        return self.__str__()
