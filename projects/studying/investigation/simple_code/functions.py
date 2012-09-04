__author__ = 'rpm'

print("---------------  functions  -------------")

print("---------------  ENVIRONMENT  -------------")
print("scopes in functions have self cope and has no overrides global scope")

glO={"ono":1, "two":2, "three":3}

def length(map):
    """ This is documentation comment """
    return len(map)
def newO() :
    glO={1:"one", 2:"two", 3:"three"}
    return glO

print(glO)
print(newO())

def fin() :
    print("First method")

def fin() :
    print("second method")

fin()

def deff(one="f", two="t") :
    print(one)
    print(two)

def search_product(dic, find) :

    if not type(dic) == type({}) :
        return -1

    counter = 0

    for val in dic.values() :
        if val == find :
            counter += 1
    return counter

find = "ono"
dic = {1:"ono", 2:"neono", 3:"osyou", 4:"ono"}
print("searched products: %s" % search_product(dic, find))
deff("one", "two")

# Functions inside other functions
def make_omlet(map) :

    def findA() :
        result = 0
        for key in map.keys() :
            for char in map[key] :
                if char == 'a' or char == 'A' :
                    result += 1
        return result

    result = findA()

    if not result:
        print("Oh no!!! there is no A")
    else :
        print("fine, result = " + str(result))

make_omlet({"1" : "Ano", "2" : "Twano"})









