import operator

def combine(a,b,op):
    return op(a,b)

result = combine(10,5,operator.add)
print(result)

result = combine(10,5,operator.mul)
print(result)