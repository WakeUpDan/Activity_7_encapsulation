class Car:
    def __init__(self, year_model, make):
        # Initialize data attributes with double underscores for encapsulation
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        # Add 5 to the speed data attribute
        self.__speed += 5

    def brake(self):
        # Subtract 5 from the speed data attribute
        self.__speed -= 5

    def get_speed(self):
        # Return the current speed
        return self.__speed

def main():
    # Design a program that creates a Car object
    # Passing sample data for year model and make
    my_car = Car("2024", "Toyota")

    print("--- Accelerating ---")
    # Call the accelerate method five times
    for i in range(5):
        my_car.accelerate()
        # After each call, get the current speed of the car and display it
        print(f"Current speed: {my_car.get_speed()}")

    print("\n--- Braking ---")
    # Call the brake method five times
    for i in range(5):
        my_car.brake()
        # After each call, get the current speed of the car and display it
        print(f"Current speed: {my_car.get_speed()}")

# Execute the main program
if __name__ == "__main__":
    main()