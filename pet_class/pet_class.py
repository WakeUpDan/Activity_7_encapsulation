class Pet:
    def __init__(self, name="", animal_type="", age=0):
        # Initialize data attributes with double underscores for encapsulation
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    # --- Mutator (Setter) Methods ---
    def set_name(self, name):
        # Assigns a value to the __name field
        self.__name = name 
    def set_animal_type(self, animal_type):
        # Assigns a value to the __animal_type field
        self.__animal_type = animal_type
    def set_age(self, age):
        # Assigns a value to the __age field
        self.__age = age

# --- Accessor (Getter) Methods ---
    def get_name(self):
        # Returns the value of the __name field
        return self.__name
    def get_animal_type(self):
        # Returns the value of the __animal_type field
        return self.__animal_type
