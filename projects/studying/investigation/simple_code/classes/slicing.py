"""
Slicing operations
"""

def div_sep(msg = "") :
    div_symbol = "#" * 10
    print('')
    print(div_symbol , msg, div_symbol)

def sub_div(msg = "") :
    div_symbol = "-" * 10
    print('')
    print(div_symbol, msg, div_symbol)

a = ["spam", "eggs", 100, 24]
div_sep("Slicing operations " + str(a))

sub_div(" negative values a[1 : -1]")
print(a[1 : -1])

sub_div("print all still 2 element a[ : 2]")
print (a[ : 2])

sub_div("print all instead first 2 elements a[ 2 : ]")
print (a[2 : ])

sub_div("a.extend(a)")
a.extend(a)
print a

sub_div("show elements from 2 to 5 a[2 : 5]")
print(a[2 : 5])

sub_div("copy list b=a[:]")
b = a[ : ]
print(str(b))

div_sep("insert operations")

sub_div("multiple adding a[0 : 2] = [1, 24]")
a[0 : 2] = [1, 24]
print (a)

sub_div("insert some a[1 : 1] = hello")
a[1 : 1] = "hello"
print(a)

sub_div("remove some a[1 : 6] = []")
a[1 : 6] = []
print(a)

stri = []
stri[0 : 0] = "hello"
stri.reverse()

rstr = ""
for s in stri :
    rstr += s

print(rstr)





