####################  NAMES  ################
print("------------NAMES-----------")
print("")
str_1="hello"
str_2="world"
print(str_1, str_2)
type(str_1)

# also you could set different types to existing members. Buut it's a bad practice.
str_1=1
print(str_1 + 1)

# linking - values is being copying
link1=50
link2=link1
link1=30
print(link2)

####################  TUPLES  #################
print("")
print("----------------TUPLES---------------")
print("")
# Tuples - immutable sequences of data "like filal array in java"
# You can't change tupe after first assignment like tup[5]="fifth"

tuple=("hel", "lo", " ", "worl", "d", 150)
tupleString="Tuple starts: %s%s%s%s%s%d" % tuple
print(tuple)
print(tupleString)

# tuples can be used as arrays in java 0 - style.
print("sixth tupe value", tuple[5])
# get length of tuple - works like a java array length
print("tuple length", len(tuple))

tuple1=("one", "second", "thirt", "4", 5, 6)

# two-dimentional tuples: accessing like in java arrays
tuple2D=(tuple, tuple1, "third element of 2d tuple")
print(tuple2D)
print(tuple2D[1][2])
print(tuple2D[2])

# single tuple element.
oneTuple=("One tuple", ) # "," is a must. Otherwize it will be str object.
print(oneTuple)

# get pieces of tuples and lists also it can be applied to strings
slice=tuple1[2:5]
print(slice)

##################  LISTS  #################
print("")
print("-------------LISTS------------------")
print("")
# lists - mutable tuples - the difference is in declaration
breakfest= ["cofee", "tea", "egg", "bread"]
print(breakfest)
print(breakfest[2])
breakfest[2]="changed value"
print(breakfest[2])
print("list length", "=", len(breakfest))

# append elements - can append just one element at once
breakfest.append("append1")
breakfest.append("append etc..")
print(breakfest)

# add more then one element at once.
breakfest.extend(["ext1", "ext2"])

# remove item from list
print("breakfest length", len(breakfest))
print("pop from list item " + str(len(breakfest) - 1), breakfest.pop(len(breakfest) - 1))
print("breakfest length", len(breakfest))

########### DICTONARIES (Maps) #############
print("")
print("-------------DICTONARIES------------------")
print("")
# creating
simple_dict = {}
simple_dict["key1"]="value1"
simple_dict["key2"]="value2"

print(simple_dict)
print("dic value by key1:", simple_dict["key1"])

# init with declaration
dic1={"key1" : "value1",
	"key2" : "value2",
	"key3" : "value3"}
	
print(dic1)
dic1["key1"]="changed value"
print(dic1["key1"])
print("dic1 length: ", len(dic1), "simple_dic length: ", len(simple_dict))

# use numbers as keys

dic1={1 : "number value1",
	2 : "number value2",
	3 : "number value3"}
	
print(dic1)
print("accessing by numbers ", dic1[2])

# getting keys from a dictionary
d_keys=dic1.keys()
d_values=dic1.values()

print("keys type: ", type(d_keys))
print("values type: ", type(d_values))

print("dic keys: \n", d_keys)
print("dic values: \n", d_values)

# list method
print("dic keys: \n", list(d_keys))
print("dic values: \n", list(d_values))

######### TREATING STRINGS AS A LIST ###########
print("")
print("--------- TREATING STRINGS AS A LIST -----------")
print("")

#slicing do dividing strings into different characters
name="hello"
print("slice of string = ", name[4])
names=["Ivan", "Ivanov"]
print(names[0][0], names[0])
print("String length: ", len(name))

################### SPECIAL TYPES #####################
print("")
print("---------------- SPECIAL TYPES ------------------")
print("")

# None - like null in java
print(None)

# true and false values - 1 and 0.
print(True)
print(False)
print(0 + False)
print(0 + True)

print("0 == False", 0 == False)
print("True > False", True > False)
print("etc ....")

##################### SETS ######################
print("")
print("---------------- SETS ------------------")
print("")

#sets is a list but there is no equal values
set1=["first", "second", "first", "third"]
print("List representation", set1)
print("Set representation", set(set1))




















