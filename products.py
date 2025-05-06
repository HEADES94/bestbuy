class Product:
    """
    A Product class that represents a product in the store.
    Includes name, price, quantity, and active status.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a Product instance.

        :param name: Product name (must be a non-empty string).
        :param price: Product price (float, must be non-negative).
        :param quantity: Product quantity (int, must be non-negative).
        :raises ValueError: If inputs are invalid.
        """
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product.

        :return: Quantity as integer.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product. Deactivates the product if quantity reaches 0.

        :param quantity: New quantity (must be >= 0).
        :raises ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Returns whether the product is active.

        :return: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self) -> str:
        """
        Prints and returns a string representation of the product.

        :return: Product details as string.
        """
        info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        print(info)
        return info

    def buy(self, quantity) -> float:
        """
        Buys a specified quantity of the product.

        :param quantity: Number of items to buy (must be > 0 and <= available quantity).
        :return: Total price as float.
        :raises ValueError: If quantity is invalid or exceeds stock.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock to complete the purchase.")
        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price


# Test code (for demonstration purposes)
if __name__ == '__main__':
    # Create two Product instances
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    # Make purchases
    print(bose.buy(50))          # Expect 12500
    print(mac.buy(100))          # Expect 145000

    # Check if Mac is still active (should be False now)
    print(mac.is_active())

    # Show current state of products
    bose.show()
    mac.show()

    # Update quantity of Bose and show again
    bose.set_quantity(1000)
    bose.show()
