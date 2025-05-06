import products
import store


def start(best_buy):
    """
    Starts the user interface loop for interacting with the store.

    :param best_buy: Store instance.
    """
    while True:
        print("\n--- Welcome to Best Buy ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == '1':
            print("\n--- Products in store ---")
            for product in best_buy.get_all_products():
                product.show()

        elif choice == '2':
            total_quantity = best_buy.get_total_quantity()
            print(f"\nTotal quantity of all products: {total_quantity}")

        elif choice == '3':
            shopping_list = []
            all_products = best_buy.get_all_products()

            print("\nAvailable products:")
            for idx, product in enumerate(all_products):
                print(f"{idx + 1}. {product.name}")

            print("Enter the product numbers and quantities you want to buy.")
            print("Type 'done' when finished.")

            while True:
                product_input = input("Enter product number (or 'done'): ")
                if product_input.lower() == 'done':
                    break

                try:
                    product_idx = int(product_input) - 1
                    if product_idx < 0 or product_idx >= len(all_products):
                        print("Invalid product number. Try again.")
                        continue

                    quantity = int(input("Enter quantity: "))
                    product = all_products[product_idx]
                    shopping_list.append((product, quantity))

                except ValueError:
                    print("Invalid input. Please enter numbers.")

            if shopping_list:
                try:
                    total_price = best_buy.order(shopping_list)
                    print(f"\nOrder successful! Total cost: {total_price} dollars.")
                except Exception as e:
                    print(f"Error processing order: {e}")
            else:
                print("No products selected for order.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == '__main__':
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)
