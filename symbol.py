from newline import newline_matching

class Node:

    def eval(self):
        pass

    def get_tree(self):
        pass

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Num(other)
        return Add(self, other)

    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Num(other)
        return Add(other, self)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Num(other)
        return Mul(self, other)

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Num(other)
        return Mul(other, self)
    
    def __pow__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Num(other)
        return Pow(self, other) 

    def __rpow__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Num(other)
        return Pow(other, self)  

    def __call__(self, x):
        return self.eval(x)

    def __str__(self):
        pass

        


class Num(Node):
    def __init__(self, val):
        self.val = val

    def eval(self, x):
        return self.val
    
    def __str__(self):
        return f"{self.val}"
    
    def get_tree(self):
        return f"{self.val}"
    


class Symbol(Node):
    def __init__(self, symbol: str = "x"):
        self.symbol = symbol

    def eval(self, x):
        return x
        
    def __str__(self):
        return f"{self.symbol}"
    
    def get_tree(self):
        return f"{self.symbol}"
    
    

class Add(Node):

    def __init__(self, left, right):
        self.left = left 
        self.right = right

    def eval(self, x):
        return self.left.eval(x) + self.right.eval(x)

    def __str__(self):
        return f"{self.left} + {self.right}"
    
    def get_tree(self):
        s, spaces, op1, op2 = newline_matching(self.left.get_tree(), self.right.get_tree())
        row1_space = " "*((op1+spaces+op2)//2)
        op1_space = " "*op1
        op2_space = " "*(spaces-op1+op2-1)
        return f"{row1_space}+ \n{op1_space}/{op2_space}\\\n{s}"  



class Mul(Node):
    
    def __init__(self, left, right):
        self.left = left 
        self.right = right

    def eval(self, x):
        return self.left.eval(x) * self.right.eval(x)
    
    def __str__(self):
        return f"({self.left})⋅({self.right})"
    
    def get_tree(self):
        s, spaces, op1, op2 = newline_matching(self.left.get_tree(), self.right.get_tree())
        op1_space = " "*op1
        op2_space = " "*(spaces-op1+op2-1)
        row1_space = " "*((op1+spaces+op2)//2)
        return f"{row1_space}+ \n{op1_space}/{op2_space}\\\n{s}"  



class Pow(Node):
    def __init__(self, base: Node, exp: Node):
        self.base = base
        self.exp = exp

    def eval(self, x):
        return self.base.eval(x) ** self.exp.eval(x) 

    def __str__(self):
        return f"({self.base})^({self.exp})"
    
    def get_tree(self):
        s, spaces, op1, op2 = newline_matching(self.base.get_tree(), self.exp.get_tree())
        row1_space = " "*((op1+spaces+op2)//2)
        op1_space = " "*op1
        op2_space = " "*(spaces-op1+op2-1)
        return f"{row1_space}^ \n{op1_space}/{op2_space}\\\n{s}"   



class Comp(Node):

    def __init__(self, outer, inner):
        self.outer = outer 
        self.inner = inner

    def eval(self, x):
        pass
        


class Expression:

    def __init__(self, tree: Node):
        self.tree = tree




# tree = Pow(Add(Num(2), Num(3)), Symbol())
# print(tree.eval(10))

x = Symbol()
f = 2*x + x**3 + 2 * (x+3) + 2*x**4
print(f.get_tree())



# f(x) = 2x * exp(cos(x))
#           mul 
#     mul          comp
# num(2) sym(x) exp     comp
#                   cos     sym(x)
# 
#
#comp: 
# exp, trig, abs
#
# mul
# add
# pow
# frac
# log_n
# 
# förenkling av trädet
# 
# f(x) = 1/x
#
#       
#

