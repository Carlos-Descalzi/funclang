# funclang
A small functional language interpreter similar to Haskell implemented in python and ANTLR4, done just for self-learning.

Some examples:
```
    x(a,b): a + b; 
    print(x(1,2));
    
    fib(x): x <= 1 ? x : (fib(x-1)+fib(x-2));
    print(fib(5),fib(6),fib(7),fib(8));


    # recursively walk through lists
    printlines(x): 
        x ? { h, t = split(x) ; print(x) ; printlines(x) }
          : 1;

    items=[1,2,3,4,5,6];
    printlines(items);

    # passing list as parameters
    do_something(a,b,c,d,e,f,g): 1

    do_something($items);

    # Functions as first class objects
    x(a,b): a + b;
    z(f,a,b): f(a,b);
    print("function as first class object:",z(x,1,2));

    # Lists
    max(x): x 
        ? { h,t=split(x); m=max(t); h > m ? h : m } 
        : 0;

    sum(x) : x ? {h,t=split(x); h+sum(t)} : 0;
    
    print(max(items));
    print(sum(items));

```
All functions return a value, even builtin functions.
Assignment returns always 1.
print returns always 1.
One difference with Haskell is there is no pattern matching.

## Operators
```
+, -, *, /, **: arithmetic operators
|, &, ^: bitwise/boolean operators
~: 2 complement.
!: logical negation.
$: convert a list into parameters for a function.
>,>=,<,<=,==: comparation.
(expr) ? (expr1) : (expr2) : if/else

```

## Built-in functions
```
split(list): returns the list splitted into head and tail
map(func, list): returns the mapping of a function over a list
print(...): prints parameters
```
