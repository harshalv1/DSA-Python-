

class Example:
    def __init__(self):
        self._value = 0

    # Getter method
    def get_value(self):
        return self._value

    # Setter method
    def set_value(self, new_value):
        if new_value >= 0:
            self._value = new_value
        else:
            print("Invalid value. Please provide a positive integer.")

example = Example()

# Use the getter to retrieve the property value
print(example.get_value())  # Output: 0

# Use the setter to assign a new value
example.set_value(10)

# Use the getter again to retrieve the updated value
print(example.get_value())  # Output: 10

# Try to set an invalid value
example.set_value(-5)       # Output: Invalid value. Please provide a positive integer.

# The value remains unchanged
print(example.get_value())  # Output: 10
