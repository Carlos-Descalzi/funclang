# funclang
A small functional language interpreter similar to Haskell implemented in python and ANTLR4, done just for self-learning.

Some examples:
```
    x(a,b): a + b; 
    print(x(1,2));
    
    fib(x): x <= 1 ? x : (fib(x-1)+fib(x-2));
    print(fib(5),fib(6),fib(7),fib(8));
```
