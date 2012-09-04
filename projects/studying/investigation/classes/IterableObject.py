__author__ = 'rpm'

class IterableObject :
    counter=0

    def __init__(self, iterableElements) :
        self.data = range(iterableElements)
        pass
    def __iter__(self):
        return self
    def next(self):
        next = self.counter
        self.counter += 1
        if self.counter > len(self.data) :
            raise StopIteration

        return self.data[next]

cls = IterableObject(20)
for element in cls :
    print element

xvec = [10, 20, 30]
print zip(xvec)

