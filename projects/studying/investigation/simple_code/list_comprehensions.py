squares=[]

for x in range(10) :
    squares.append(x**2)

print(squares)
squares=[x**3 for x in range(10)]
print(squares)

squares = [-1, 1, 2, 3]

print([x for x in squares if x <= 0])
print([abs(x) for x in squares])

a = "a"
# remove object
del a

#print(a) will cause error - NameError: name 'a' is not defined
a = list("aaa")
b = list("aaa")

print(a is b)
del b
b = list("aaa")
print(a in b)

