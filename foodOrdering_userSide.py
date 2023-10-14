class FoodOrderingApp:
    def __init__(self):
        self.customers = {}
        self.food_items = {
            1: {"name": "Tandoori Chicken (4 pieces)", "price": 240},
            2: {"name": "Vegan Burger (1 Piece)", "price": 320},
            3: {"name": "Truffle Cake (500gm)", "price": 900}
        }

    def register_customer(self):
        print("\n--- Welcome to Our Food Ordering App ---")
        print("\n****** Customer Registration ******")
        full_name = input("Enter your Full Name: ")
        mobile_no = input("Enter your Mobile Number: ")
        email = input("Enter your Email Address: ")
        address = input("Enter your Delivery Address: ")
        password = input("Choose a Strong Password: ")

        customer_id = len(self.customers) + 1
        self.customers[customer_id] = {
            "Full Name": full_name,
            "Mobile Number": mobile_no,
            "Email Address": email,
            "Delivery Address": address,
            "Password": password,
            "Orders": []
        }
        print("\nRegistration completed. Thank you for joining us!")

    def login_customer(self):
        print("\n****** Customer Login ******")
        email = input("Enter Your Email Address: ")
        password = input("Enter Your Password: ")

        for customer_id, details in self.customers.items():
            if details["Email Address"] == email and details["Password"] == password:
                print("*** Login Successful ***")
                print("You are now ready to place an order.")
                self.place_order(customer_id)
                return

        print("\nEmail or Password is incorrect. Please try again.")
        self.login_customer()

    def place_order(self, customer_id):
        print("\n--- Place a New Order ---")
        print("Available Food Items:")
        for key, item in self.food_items.items():
            print(f"{key} - {item['name']} [Price: INR {item['price']}]")

        try:
            order_choice = int(input("Enter the number of the item you want to order: "))

            if order_choice in self.food_items:
                food_item = self.food_items[order_choice]
                print("Your order:", food_item["name"])
                self.customers[customer_id]["Orders"].append(food_item)
                print("\nYour order is placed! Thank you for ordering.")
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run(self):
        print("\n--- Welcome to Our Food Ordering App ---")
        self.register_customer()
        self.login_customer()


if __name__ == "__main__":
    app = FoodOrderingApp()
    app.run()
