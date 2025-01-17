from newline import newline_matching
import math

class Node:

    def eval(self):
        pass

    def get_tree(self):
        pass

    def diff(self):
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

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Num(other)
        return Div(self, other)
    
    def __rtruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Num(other)
        return Div(other, self)

        


class Num(Node):
    def __init__(self, val):
        self.val = val

    def eval(self, x):
        return self.val
    
    def __str__(self):
        return f"{self.val}"
    
    def get_tree(self):
        return f"{self.val}"
    
    def diff(self):
        return Num(0)


class Symbol(Node):
    def __init__(self, symbol: str = "x"):
        self.symbol = symbol

    def eval(self, x):
        return x
        
    def __str__(self):
        return f"{self.symbol}"
    
    def get_tree(self):
        return f"{self.symbol}"
    
    def diff(self):
        return Num(1)
    
    

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

    def diff(self):
        return Add(self.left.diff(), self.right.diff())


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
        return f"{row1_space}⋅ \n{op1_space}/{op2_space}\\\n{s}"  
    
    def diff(self):
        return Add(Mul(self.left.diff(), self.right), Mul(self.left, self.right.diff()))

class Div(Node):

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def eval(self, x):
        return self.numer.eval(x) / self.denom.eval(x)
    
    def __str__(self):
        return f"({self.numer})/({self.denom})"

    def get_tree(self):
        s, spaces, op1, op2 = newline_matching(self.numer.get_tree(), self.denom.get_tree())
        op1_space = " "*op1
        op2_space = " "*(spaces-op1+op2-1)
        row1_space = " "*((op1+spaces+op2)//2)
        return f"{row1_space}/ \n{op1_space}/{op2_space}\\\n{s}"  

    def diff(self):
        new_numer = Add(Mul(self.numer.diff(), self.denom), Mul(Num(-1), Mul(self.numer, self.denom.diff())))
        new_denom = Pow(self.denom, Num(2))
        return Div(new_numer, new_denom)


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
    
    def diff(self):
        # a = Mul(self.exp.diff(), Ln(self.base))
        # b = Div(Mul(self.exp, self.base.diff()), self.base)
        return Mul(self, Add(Mul(self.exp.diff(), Ln(self.base)), Div(Mul(self.exp, self.base.diff()), self.base)))

class Ln(Node):
    def __init__(self, arg: Node):
        self.arg = arg
    
    def eval(self, x):
        return math.log(self.arg.eval(x))
    
    def __str__(self):
        return f"ln({self.arg})"
    
    def get_tree(self):
        arg_tree = self.arg.get_tree()
        arg_tree_arr = arg_tree.split("\n")
        len_row = len(arg_tree_arr[0])
        spaces = " "*(len_row//2)
        return f"{spaces}ln \n{spaces}| \n{arg_tree}" 
    
    def diff(self):
        return Div(self.arg.diff(), self.arg)


        


class Expression:

    def __init__(self, tree: Node):
        self.tree = tree


breakpoint()

# tree = Pow(Add(Num(2), Num(3)), Symbol())
# print(tree.eval(10))

# x = Symbol()
# f = 3*x + x + x*x
# print(f)
# print(f.diff())
# print(f.diff()(3))




# f(x) = 2x * exp(cos(x))
#           mul 
#     mul          comp
# num(2) sym(x) exp     comp
#                   cos     sym(x)
# 
#

#
#

