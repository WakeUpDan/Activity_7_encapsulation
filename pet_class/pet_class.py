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
    def get_age(self):
        # Returns the value of the __age field
        return self.__age
    
def main():
    # 1. Create an object of the Pet class
    user_pet = Pet()
    # 2. Prompt the user to enter the name, type, and age of their pet
    print("Please enter your pet's details:")
    input_name = input("Pet's Name: ")
    input_type = input("Animal Type (e.g., Dog, Cat, Bird): ")
    input_age = input("Pet's Age: ")

    # 3. Store this data as the object's attributes using the setter methods
    user_pet.set_name(input_name)
    user_pet.set_animal_type(input_type)
    user_pet.set_age(input_age)

    # 4. Use the object's accessor methods to retrieve and display the data
    print("\n--- Pet Information ---")
    print(f"Name:        {user_pet.get_name()}")
    print(f"Animal Type: {user_pet.get_animal_type()}")
    print(f"Age:         {user_pet.get_age()}")


# Execute the main program
if __name__ == "__main__":
    main()

