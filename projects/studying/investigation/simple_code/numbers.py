# type() method - using to determinate type of data.
type(1)
type(1.1)
type("Hello")
# мнимое число - хз что это такое
type(11j)

# Include numbers into strings
print("Hello " + str(10 + 5) + " " + "world")
print("hello %f world" %(5+5))
#or strict output to 2 symbols before dot and two after it.
print("hello %2.2f" %(10/3))
print("insert numbers and strings into strings with special patterns %%d %%f %%s  %d %f %s" %(5000, 123.123, "str"))
#or with E number
print("Nubmer in E format 1.212121E+01 %%E: %E" % 12.12121212)
# calculating
print("calculations")
print(2+2)
print(2+2*2)
print((2+2)*2)
print((2+2)*2 / 4 + 8)
# but 3 / 4 will be 0. You should use float(3) / 4
print("float")
print(float(3)/4)
print(4%3)
# octal numbers
print("octal number format %d %o" %(10, 10))
#hex
print("hex number format %d %x %X" % (10, 10, 10))

