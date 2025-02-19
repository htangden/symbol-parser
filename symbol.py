from newline import newline_matching
import math

class Node:

    def eval(self):
        pass

    def get_tree(self):
        pass

    def diff(self):
        pass

    def prune(self):
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
        return Mul(self, Pow(other, Num(-1)))
    
    def __rtruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Num(other)
        return Mul(other, Pow(self, Num(-1)))

        


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
    
    def prune(self):
        return self


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
    
    def prune(self):
        return self
    
    

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
        return Add(self.left.diff(), self.right.diff()).prune()
    
    def prune(self):
        pruned_left = self.left.prune()
        pruned_right = self.right.prune()

        if isinstance(pruned_right, Num) and isinstance(pruned_left, Num):
            return Num(pruned_left.val + pruned_right.val)
        
         # f(x) + 0 = f(x)
        if isinstance(pruned_right, Num):
            if pruned_right.val == 0:
                return pruned_left
        elif isinstance(pruned_left, Num):
            if pruned_left.val == 0:
                return pruned_right
            
        return Add(pruned_left, pruned_right)



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
        return Add(Mul(self.left.diff(), self.right), Mul(self.left, self.right.diff())).prune()
    
    def prune(self):
        pruned_left = self.left.prune()
        pruned_right = self.right.prune()


        if isinstance(pruned_right, Num) and isinstance(pruned_left, Num):
            return Num(pruned_left.val * pruned_right.val)
        
        # f(x) * 0 = 0 || f(x) * 1 = f(x)
        if isinstance(pruned_right, Num):
            if pruned_right.val == 0:
                return Num(0)
            if pruned_right.val == 1:
                return pruned_left
        elif isinstance(pruned_left, Num):
            if pruned_left.val == 0:
                return Num(0)
            if pruned_left.val == 1:
                return pruned_right                         

        return Mul(pruned_left, pruned_right)   



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
        return Mul(self, Add(Mul(self.exp.diff(), Ln(self.base)), Mul(Mul(self.exp, self.base.diff()), Pow(self.base, Num(-1))))).prune()

    def prune(self):
        pruned_base = self.base.prune()
        pruned_exp = self.exp.prune()

        if isinstance(pruned_exp, Num):
            if pruned_exp.val == 0:
                return Num(1)
            if pruned_exp.val == 1:
                return pruned_base
        
        if isinstance(pruned_base, Num):
            if pruned_base.val == 0:
                return Num(0)
            if pruned_base.val == 1:
                return Num(1)

        return Pow(pruned_base, pruned_exp)

class Ln(Node):
    def __init__(self, arg: Node):
        if isinstance(arg, int) or isinstance(arg, float):
            arg = Num(arg)
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
        return Mul(self.arg.diff(), Pow(self.arg, Num(-1))).prune()
    
    def prune(self):
        pruned_arg = self.arg.prune()

        if isinstance(pruned_arg, Num):
            return Num(math.log(pruned_arg.val))
        return Ln(pruned_arg)
 

if __name__ == "__main__":
    x = Symbol()
    breakpoint()