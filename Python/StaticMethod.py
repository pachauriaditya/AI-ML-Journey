'''
Static Method

-> No compulsory parameter (self or cls).
-> Cannot directly access instance attributes (self) or class attributes (cls).
-> Used when a method performs only a utility task (e.g., calculation).
-> Decorator used: @staticmethod
'''

class Laptop:

    # Class Attribute
    storage_type = "SSD"

    # Constructor (Initializes instance attributes)
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    # Class Method
    # Used to access class attributes.
    @classmethod
    def get_storage_type(cls):
        print(f"Storage Type: {cls.storage_type}")

    # Static Method
    # Approach:
    # 1. Takes only the required input parameters.
    # 2. Performs discount calculation.
    # 3. Does not use self or cls.
    # 4. Prints the final discounted price.
    @staticmethod
    def cal_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"Discounted Price: {final_price}")


# Object Creation
ll = Laptop("16GB", "1TB")

# Calling Static Method
ll.cal_discount(40_000, 10)