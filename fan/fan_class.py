class Fan:
        # Constants for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        # Private data fields using __ prefix for encapsulation
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = color
        self.__on = on

# --- Accessor (Getter) Methods ---
    def get_speed(self):
        return self.__speed

    def get_on(self):
        return self.__on
    
    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color


# --- Mutator (Setter) Methods ---
    def set_speed(self, speed):
        self.__speed = speed

    def set_on(self, on):
        self.__on = on
    
    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = color

def TestFan():
    # 1. Create first Fan object
    # Assign maximum speed, radius 10, color yellow, and turn it on.
    fan1 = Fan(speed=Fan.FAST, radius=10.0, color="yellow", on=True)
    # 2. Create second Fan object
    # Assign medium speed, radius 5, color blue, and turn it off.
    fan2 = Fan(speed=Fan.MEDIUM, radius=5.0, color="blue", on=False)

# 3. Display properties using getter methods
    print("--- Fan 1 Properties ---")
    print(f"Speed:  {fan1.get_speed()}")
    print(f"Radius: {fan1.get_radius()}")
    print(f"Color:  {fan1.get_color()}")
    print(f"Is On:  {fan1.get_on()}\n")

    print("--- Fan 2 Properties ---")
    print(f"Speed:  {fan2.get_speed()}")
    print(f"Radius: {fan2.get_radius()}")
    print(f"Color:  {fan2.get_color()}")
    print(f"Is On:  {fan2.get_on()}")

# Execute the test program
if __name__ == "__main__":
    TestFan()