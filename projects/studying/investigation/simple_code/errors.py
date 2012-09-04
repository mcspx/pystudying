# exceptions
map={"one":1, "two":2}
try:
    threee=map["two"]
except KeyError as error :
    print("error type", error)
    print("tete is no %s" % error)
else :
    print("all is ok")
finally :
    print("finally )))")

# Throw exceptions
def ifNotMapThrow(map) :
    if type(map) == type({}) :
        print("Right argument")
    else :
        raise TypeError("This argument not supported - %s " % str(map))

ifNotMapThrow("")
print("This should not appear )")
