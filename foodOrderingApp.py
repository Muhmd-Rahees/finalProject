class FoodCourt:
    def __init__(self):
        self.food = {}
        self.food_id = 1  # Initialize the first food ID
        self.personal_details = {}
        self.customer_id = 1  # Initialize the first customer ID

    def food_card(self):
        food_name = input("Enter food name: ")
        quantity = float(input("Enter food quantity: "))
        price = float(input("Enter food price: "))
        discount = float(input("Enter food discount: "))
        stock = float(input("Enter your stock:"))
        
        # Create a dictionary for the food item
        item = {
            "Name": food_name,
            "Quantity": quantity,
            "Price": price,
            "Discount": discount,
            "Stock": stock
        }
        
        # Assign the food ID and add the item to the food dictionary
        self.food[self.food_id] = item
        self.food_id += 1  # Increment the food ID
        print("********** ITEM ADDED **********")

    def delete_food_card(self):
        food_id = int(input("Enter the food ID you want to delete: "))
        if food_id in self.food:
            del self.food[food_id]
            print(f"Food item with ID {food_id} deleted.")
        else:
            print(f"Food item with ID {food_id} not found.")

    def update_food_card(self):
        food_id = int(input("Enter the food ID for updating: "))
        if food_id in self.food:
            for key in self.food[food_id]:
                new_value = input(f"Enter new {key} value: ")
                self.food[food_id][key] = new_value
            print("Food item updated:", self.food[food_id])
        else:
            print(f"Food item with ID {food_id} not found.")

if __name__ == "__main__":
    obj = FoodCourt()
    obj.food_card()
    obj.update_food_card()
    obj.delete_food_card()
