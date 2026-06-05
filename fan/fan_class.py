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

