__author__ = 'Babayev Ilyas'

class Fridge :
    """This class is first class on the Python language
    Methods:
    has(food_name[, quantity]) check is something in the fridge
    add_one(food_name)
    add_many(food_dict)
    get_one(food_name)
    get_many(food_dict)
    get_ingredients(food)
    """

    def __init__(self, items={}) :
        """
        Hello
        """
        if type(items) != type({}) :
            raise TypeError("Fridge requires dictionary but received %s" % type(items))

        self.items=items
        return

    def __inner(self) :
        print("Hello from inner")

    def out(self) :
        self.__inner()

fridge = Fridge({"1" : "1"})
fridge.out()

class Abs :
    def __init__(self):
        None

    def ono(self) :
        ...




