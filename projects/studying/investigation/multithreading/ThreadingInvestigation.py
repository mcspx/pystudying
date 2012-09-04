# coding=utf-8
import threading

__author__ = 'rpm'

class MyThread(threading.Thread) :
    def __init__(self, name="thread"):
        super(MyThread, self).__init__(name=name)
#        self.setDaemon(True)

    def run(self) :
        while True :
            print self.getName()

if __name__ == "__main__" :
    thread1 = MyThread("***")
    thread2 = MyThread("###")

#    thread1.start()
#    thread2.start()
print(unicode("вет", "UTF-8", 'strict'))
str = u"привет"
print(str)
print(len(str))


