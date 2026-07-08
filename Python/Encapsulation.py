'''
Encapsulation:
- Wrapping data (variables) and methods (functions) into a single unit (class).
- It also helps in hiding data from the outside world.

Access Modifiers in Python:
1. Public Members    -> Accessible from anywhere.
2. Protected Members -> Accessible within the class and its subclasses (convention: _variable).
3. Private Members   -> Accessible only within the class (name mangling: __variable).
'''

class BankAccount:

    # Constructor to initialize account details
    def __init__(self, account_number, balance):
        self.account_number = account_number   # Public member
        self._balance = balance                # Protected member
        self.__pin = None                      # Private member

    # Method to set the account PIN
    def set_pin(self, pin):
        self.__pin = pin

    # Method to check PIN and return balance
    def get_balance(self, pin):
        # Check if entered PIN matches the stored PIN
        if pin == self.__pin:
            return self._balance
        else:
            return "Invalid PIN"


# ================= Example Usage =================

# Create a BankAccount object
account = BankAccount("123456789", 1000)

# Set the account PIN
account.set_pin("1234")

# Access balance using the correct PIN
print(account.get_balance("1234"))   # Output: 1000

# Access balance using the wrong PIN
print(account.get_balance("1111"))   # Output: Invalid PIN