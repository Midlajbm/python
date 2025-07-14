def generator():
    yield 1
    yield 2
    yield 3
res=generator()     # CREATING OBJECT FOR GENERATOR
print(res)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
