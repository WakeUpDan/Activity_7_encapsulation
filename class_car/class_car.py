class Car:
    def __init__(self, year_model, make):
        # Initialize data attributes with double underscores for encapsulation
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
