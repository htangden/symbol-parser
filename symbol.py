
class Node:

    def eval(self):
        pass


class Num(Node):
    def __init__(self, val):
        self.val = val

    def eval(self, x):
        return self.val
    
class Add(Node):

    def __init__(self, left, right):
        self.left = left 
        self.right = right

    def eval(self, x):
        return self.left.eval(x) + self.right.eval(x)

class Mul(Node):

    def __init__(self, left, right):
        self.left = left 
        self.right = right

    def eval(self, x):
        return self.left.eval(x) * self.right.eval(x)
    
class Pow(Node):
    def __init__(self, base: Node, exp: Node):
        self.base = base
        self.exp = exp

    def eval(self, x):
        return self.base.eval() ** self.exp.eval() 

class Comp(Node):

    def __init__(self, outer, inner):
        self.outer = outer 
        self.inner = inner

    def eval(self, x):
        pass
        



class Expression:

    def __init__(self, tree: Node):
        self.tree = tree

class Symbol(Node):

    # def __mul__(self, other_thing):
    #     if other_thing is int or other_thing is float:
    #         return 
    def eval(self, x):
        return x


tree = Add(Mul(Num(2), Num(3)), Symbol())
print(tree.eval(10))

