def outer_func(x):
    def inner_func():
        return x
    x=x+5
    return inner_func
result = outer_func(6)
print(result)
