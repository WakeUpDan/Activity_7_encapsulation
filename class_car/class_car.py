class Car:
    def __init__(self, year_model, make):
        # Initialize data attributes with double underscores for encapsulation
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    def get_speed(self):
        # Return the current speed
        return self.__speed
    def accelerate(self):
        # Add 5 to the speed data attribute
        self.__speed += 5
    def brake(self):
        # Subtract 5 from the speed data attribute
        self.__speed -= 5
