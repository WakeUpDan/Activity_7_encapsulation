class Pet:
    def __init__(self, name="", animal_type="", age=0):
        # Initialize data attributes with double underscores for encapsulation
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age