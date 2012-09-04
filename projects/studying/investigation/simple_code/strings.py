#just print
print ("hello world")
#or just print "hello world1" but in files you should use only print command. Just printing is working only in interactive mode

#or
print("hello \"yess\" world2")
#or
print("""hello "can contain" world""")

#print with space and string concatenation
print("hello", "world")
#or
print("hello" + " " + "world")

############# Formatting strings ############# 
# place strings in format
print("hello %s %s" %("world", "Params"))

#display minimum ten chars, but if there is more than 10, it will print more
print("hello %s %10s" %("world", "Params"))
#inserp spaces after word
("hello %s %-10s hello" %("world", "Params"))

# upper and lower methods.
str1="HeLLo"
print(str1.upper())
print(str1.lower())
print("equalLowerCase: ", str1.lower() == str1.upper())

str1="HELLO"
str2="hello"

print("equalLowerCase: ", str1.lower() == str2.lower())
