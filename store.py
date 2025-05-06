from typing import List
from products import Product

class Store:
    """
    A Store class that manages a list of Product instances.
    Allows adding/removing products, checking quantities,
    and making multi-product orders.
    """

    def __init__(self, products: List[Product]):
        """
        Initialize the Store with a list of Product instances.

        :param products: List of Product objects.
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a new product to the store.

        :param product: Product object to add.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store if it exists.

        :param product: Product object to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.

        :return: Total quantity as integer.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """
        Returns a list of all active (available) products in the store.

        :return: List of active Product objects.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Processes a multi-product order.

        :param shopping_list: List of tuples (Product, quantity).
        :return: Total price of the order as float.
        """
        total_cost = 0
        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)
        return total_cost


# Test code (for demonstration purposes)
if __name__ == '__main__':
    from products import Product

    # Create product instances
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Initialize store with products
    best_buy = Store(product_list)

    # Get and print all active products
    products = best_buy.get_all_products()

    # Print total quantity of items in the store
    print(best_buy.get_total_quantity())

    # Place an order and print the total cost
    print(best_buy.order([(products[0], 1), (products[1], 2)]))

