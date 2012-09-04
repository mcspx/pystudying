from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from calendar import Calendar
from sqlite3.dbapi2 import Timestamp
from AbstractClass import AbstractClass

__author__ = 'rpm'

class MyClass(AbstractClass) :
    hello="Hello world"
    def __init__(self, a, b) :
        self.a = a
        self.b = b

    def say_hello(self) :
        print(self.hello)

    def replaceHello(self):
        self.say_hello="Replaced helllo"
        print self.say_hello
        del self.say_hello

if __name__ == "__main__" :
    cls = MyClass(1,2)
    cls.say_hello()

    print isinstance(cls.__class__, AbstractClass)
    import logging
    logging.debug("Debug message")
    logging.error("Error message")
    logging.info("Info message")
    logging.warning("Warning message")

#    server = MyClass(10, "hello")
#    server.say_hello()
#    server.replaceHello()
#
#    MyClass.say_hello(server)
#
#    print "class attributes: "
#    print "a : {}".format(server.a)
#    print "b : {}".format(server.b)





