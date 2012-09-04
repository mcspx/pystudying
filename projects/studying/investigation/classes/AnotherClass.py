from classes.MyClass import MyClass
from AbstractClass import AbstractClass
__author__ = 'rpm'

class AnotherClass (MyClass):

    def __init__(self) :
        pass

    def say_hello(self) :
        MyClass.say_hello(self)
        print "inherited hello"

cls = AnotherClass()
cls.say_hello()

class B:
    pass

class C(B):
    pass

class D(C):
    pass

for c in [D, C, B]:
    try:
        raise c
#    except D:
#        print "D"
#    except C:
#        print "C"
    except B:
        print "B"

