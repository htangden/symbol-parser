
**TODO förenkling av trädet**
- a⋅x + b⋅x = (a+b)⋅x
- x⋅x⋅...⋅x = x^a
- x+x+...+x = a*x
- x^a * x^b = x^(a+b)
- ✅ x^a / x^b = x^(a-b)
- polydiv

**TODO fundera på att göra om division till Mul + pow(, -1)**
- ✅ misslyckas med testcases complex1-5 då x^2 ofta vid diff blir x^3/x och då inte klarar df(0).
- ✅ kanske lättare att fixa vid pruning om både left och right till mul är pow och har samma bas.

**TODO lägg till funktioner**
- trig, abs


**TODO förbättra printing av expression**
- lägg bara till paranteser om nästa nod är av lägre prio
    - i.e om Mul.left är Add, och Mul.right är sym: return((self.left)*self.right)

**TODO lägg till test-cases**


```LÄNGRE I FRAMTIDEN```

**TODO lägg till latex rendering**

**TODO lösning av ekvationer**




