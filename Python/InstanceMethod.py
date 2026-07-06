'''
Instance Method

-> 1st parameter is always self.
-> self refers to the current object.
-> Can access both instance attributes and class attributes.
-> Used when the method works with object-specific data.
'''

class Laptop:

    # Class Attribute
    storage_type = "SSD"

    # Constructor (Initializes instance attributes)
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    # Instance Method
    # Approach:
    # 1. self refers to the current object.
    # 2. Accesses instance attributes using self.
    # 3. Accesses class attribute using ClassName.
    # 4. Prints complete laptop information.
    def get_info(self):
        print(f"RAM: {self.RAM}, Storage: {self.storage}, Storage Type: {Laptop.storage_type}")


# Object Creation
l1 = Laptop("16GB", "1TB")
l2 = Laptop("8GB", "500GB")

# Calling Instance Method
l1.get_info()
l2.get_info()