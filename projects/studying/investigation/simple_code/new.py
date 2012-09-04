def make_incrementor (n): return lambda x: x + n
a = make_incrementor(10)
print(a(10))
print(a(20))
print(a(30))

print("-------------------")

a = make_incrementor(5)
print(a(10))
print(a(20))
print(a(30))