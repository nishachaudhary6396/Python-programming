# lambda arguements: expression
add = lambda x: x+10
print(add(5))


# higher order functions :- passing a function as an arguement
def apply(func,x):
    return func(x)
def square(n):
    return n*n
print(apply(square,5))







