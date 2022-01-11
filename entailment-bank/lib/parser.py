from typing import Text, List
from .core import LispTree
import re

VARIABLE_RE_PATTERN = "[a-zA-Z0-9]"

def parse_lisp(lisp_proof: Text) -> LispTree:    
    i = -1
    tokens = lisp_proof
    tokens_length = len(lisp_proof)
    stack = list()
    variables_stack = list()
    lisp_tree = None
    after_renaming = False
    while i < tokens_length - 1:
        i += 1
        token = tokens[i]
        

        if token == "(":
            stack.append(token)
            continue
        
        if token == ")":
            lv = len(stack)
            stack.pop()

            if after_renaming and not lv <= 1:
                new_stacks = []
                for x, var in enumerate(variables_stack):
                    tree_var = var

                    if type(tree_var) == str:
                        tree_var = LispTree(var)

                    new_stacks.append(tree_var)
                    after_renaming = False

                variables_stack = new_stacks
                continue

            lisp_tree = LispTree("", lv)

            new_stacks = []
            for x, var in enumerate(variables_stack):
                tree_var = var

                if type(tree_var) == str:
                    tree_var = LispTree(var)

                if tree_var.depth > lisp_tree.depth or tree_var.depth == -1:
                    lisp_tree.add_child(tree_var)            
                    continue

                new_stacks.append(tree_var)

            variables_stack = new_stacks
            variables_stack.append(lisp_tree)
        
            continue
        
        if token == ">":
            i += 2
            token = tokens[i]
            var_name = token
            while i < tokens_length - 1 and re.match(VARIABLE_RE_PATTERN, tokens[i + 1]):
                i += 1
                token = tokens[i]
                var_name += token
                
            
            variables_stack[-1].node_name = var_name
            
            after_renaming = True
            continue

        # variable name
        if re.match(VARIABLE_RE_PATTERN, token):
            var_name = token

            while i < tokens_length - 1 and re.match(VARIABLE_RE_PATTERN, tokens[i + 1]): 
                i += 1
                token = tokens[i]
                var_name += token

            variables_stack.append(var_name)
            continue

    variables_stack[0].node_name = "H"
    return variables_stack[0]
