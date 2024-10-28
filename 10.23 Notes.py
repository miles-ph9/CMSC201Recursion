"""
Recursion is ass and buns I hate recursions but today's topic is recursions!! :D

Recursion - a process where it calls the function within itself; when the function calls itself

    Think of russian nesting dolls

But it ensures that what happens is not an infinite process

"""
"""
def infinite_rec(x):
    print(x)
    infinite_rec(x -1)
"""

def countdown(x):
      if x == 0:
          print('Blastoff!')
      else:
          #This is a recursive case
          print(x)
          countdown(x-1)

countdown(10)



"Unlike C++ or Java, Python prevents an infinite recursion from happening from stopping it "
" at around 1000 and then crashes"

"""
Factorial first 
    n! = n * (n-1)
    

A branching recursion makes more than one recursion per call instance, can end up making
    quite a lot of recursion calls 

Fibonacci next 
Fib(n) = fib(n-1) + fib(n-3)
Two base cases: fib(0) = fib(1) = 1

"""

# for loop

def Fib(n):
    seq = [0,1] # accounting for first pair of fibonnaci numbers
    for i in range(n):
        seq.append(seq[-1]+ seq[-2])

    return seq[-2]


# recursion
def fib (n):
    if n <=1:
        return n
    else:
        return fib(n - 1) + fib (n-2)

print(fib(8))
print(Fib(8))

"""
Even though for loops (iteration) is faster, it's better to use recursion
for bigger problems when they need to be condensed down 
"""

"""
In summary, recursion is a process of what happens when a function calls itself 
within itself.

Recursion is typically in an function and uses the return 

Even though it's not faster than  


"""