class Bread:
    def __init__(self, color='black', flour='first', price=0):
        self.__color = color
        self.__flour = flour
        self.__price = price

    @property
    def color(self):
        return self.__color

    @property
    def flour(self):
        return self.__flour

    @property
    def price(self):
        return self.__price

    @color.setter
    def color(self, color):
        self.__color = color

    @flour.setter
    def flour(self, flour):
        self.__flour = flour

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return (f"Bread: color = {self.__color}, "
                f"flour = {self.__flour}, "
                f"price = ${self.__price}")