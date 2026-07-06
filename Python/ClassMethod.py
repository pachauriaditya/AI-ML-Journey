'''
Class Method

-> 1st parameter is always cls.
-> cls refers to the class itself.
-> Can access only class attributes directly.
-> Used when the method works with class-level data.
-> Decorator used: @classmethod
'''

class Laptop:

    # Class Attribute
    storage_type = "SSD"

    # Constructor (Initializes instance attributes)
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    # Class Method
    # Approach:
    # 1. cls refers to the class.
    # 2. Accesses the class attribute using cls.
    # 3. Prints the storage type common to all objects.
    @classmethod
    def get_storage_type(cls):
        print(f"Storage Type: {cls.storage_type}")

    # Instance Method
    def get_info(self):
        print(f"RAM: {self.RAM}, Storage: {self.storage}, Storage Type: {Laptop.storage_type}")


# Object Creation
ll = Laptop("16GB", "1TB")

# Calling Class Method
ll.get_storage_type()
# or
# Laptop.get_storage_type()