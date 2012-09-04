import pickle
from io_investigation import Struct

FILE = "pickle.txt"

map = {"one":1, "two":2}

file = open(FILE, 'wb')
pickle.dump(map, file)
file.close()

file = open(FILE, 'rb')

map1= pickle.load(file)
file.close

print(map)
print(map1)

print("equals = " + str(map == map1))

print(Struct.a)
Struct.a = 1