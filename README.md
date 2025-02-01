# The Tängdén-Larsson symbol-parser

The symbol-parser is meant to create, evaluate and differentiate single variable algebraic expressions.

### Creating a variable

Creating a variable is done using the `Symbol` class. 

<pre>
  x = Symbol()
  # or  
  t = Symbol("t")
</pre>


### Creating expressions

After creating a symbol, expressions can be created intuitively by adding, multiplying or exponentiation Symbols, numbers and expression to one another.

<pre>
  f = 3 * x
  g = (x+2)*(x+5)**3  
  h = f + g + 2*f 
</pre>

## Expression functionality

### Evaluating expression at value

This can be done by either calling the expression at value or using `eval()` method.

<pre>
  f = 3 * x
  f(3) # returns 9
  f.eval(3) # returns 9
</pre>


### Printing expression

An expression can either be printed as a simple string

<pre>
  f = 2*(x+3)
  print(f) #prints: (2)⋅(x + 3)
</pre>

or as the internal tree-representation of the expression using the method `get_tree()`  

where `f.get_tree()`  returns:

<pre>
    ⋅
   / \
  2   +
     / \
    x   3
</pre>

### Differentiation

Calling `diff()` on an expression will return the expression for the differentiation of the expression.

<pre>
  f = 2*x**2 + 4*x + 5
  f_prime = f.diff() # = 4x + 4
</pre>

where `f_prime` just like `f` can be evaluated, printed and differentiated. 

### Pruning

To simplify an expression one can use the `prune()` method. Calling the method on an expression returns an expression which, if possible, is simpler.

<pre>
  f = 1*x + 0*x
  f = f.prune() # = x
</pre>

Pruning can be especially useful after differentiation. Pruning is still rudimentary and in early stages of development.

### Function-composition

Creating a function based on other functions works intuitively as one would hope.  
Illustrated here by creating an absolute value-function.

<pre>
  abs = (x**2)**0.5  # abs = |x|
  f = abs(2*x+3)   # f = |2x+3|
</pre>

### Built in functions

As of now the only built in function is the natural logarithm, `Ln`, but others (mainly trigonometric) will be added soon. 






