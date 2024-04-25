class ShoppingCart:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.products = {}

    def add_product(self, product_name, price):
        if product_name in self.products:
            print("Product already exists in the cart.")
        else:
            self.products[product_name] = price
            print(product_name + " added to the cart.")

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            print(product_name + " removed from the cart.")
        else:
            print("Product not found in the cart.")

    def calculate_total(self):
        total = sum(self.products.values())
        return total

    def apply_discount(self, total):
        if total >= 50000:
            return total * 0.55  # 45% discount
        elif total >= 20000:
            return total * 0.8  # 20% discount
        else:
            return total

    def checkout(self):
        total = self.calculate_total()
        total_after_discount = self.apply_discount(total)
        print("Total amount to be paid by " + self.owner_name) 
        print("after discount: " + str(total_after_discount))


# Your shopping cart

your_cart = ShoppingCart("yeshwanth")
your_cart.add_product("Smartphone", 15000)
your_cart.add_product("toys",4000)
your_cart.add_product("Laptop", 40000)
your_cart.remove_product("Smartphone")
your_cart.checkout()

# Friend's shopping cart
friend_cart = ShoppingCart("fzan")
friend_cart.add_product("Headphones", 2000)
friend_cart.add_product("Camera", 35000)
friend_cart.checkout()
