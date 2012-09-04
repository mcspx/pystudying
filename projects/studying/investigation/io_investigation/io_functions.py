import pickle

__author__ = 'rpm'

#for x in range(1,11):
#    print '{0:2d} {1:3d} {2:4d}'.format(x*x*x, x*x*x, x*x*x)

#print "hello people", "Hello".rjust(14)
#print "hello", str("Hello".rjust(14))
#
#table={"joe": 1, "rick": 2}
#print(table)
#
#for a in table.keys() :
#    print(a)

file = open("text.txt", 'r+')
print(file)
file.seek(0, 0)
#content = file.read()
#print(content)
#
#del content
for line in file :
    print line

file.write("Hello world")
file.close()

# to automatically close the file USE KEYWORD WITH

with open("text.txt", "r") as file :
    print(file.read())

print(file.closed)

# serializabling objects
with open("serializable.txt", 'w') as file :
    fin = (lambda x :  x**2 )
    pickle.dump(fin, file)

with open("serializable.txt", 'r') as file :
    fun=pickle.load(file)
    print fun(10)


