class Products:

    # Class variable (shared by all objects)
    count = 0

    # Constructor to initialize product details
    def __init__(self, name, price):
        self.name = name      # Instance variable
        self.price = price    # Instance variable

        # Increase product count whenever a new object is created
        Products.count += 1

    # Instance method -> Works with object-specific data
    def get_info(self):
        print(f"Price of {self.name} is {self.price}")

    # Class method -> Works with class variables
    @classmethod
    def get_count(cls):
        print(f"Total products: {cls.count}")

    # Static method -> Utility method (doesn't use class or object data)
    @staticmethod
    def get_discount(price, discount):
        # Calculate discounted price
        discounted_price = price - (price * discount / 100)
        return discounted_price


# ================= Example Usage =================

# Create product objects
p1 = Products("Laptop", 1000)
p2 = Products("Smartphone", 500)
p3 = Products("Tablet", 300)

# Display product information
p1.get_info()
p2.get_info()
p3.get_info()

# Display total number of products created
Products.get_count()

# Calculate and display discounted price
print(f"Discounted price of {p1.name}: {Products.get_discount(p1.price, 10)}")