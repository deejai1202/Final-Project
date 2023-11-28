# main.py
from food_ordering_operations import FoodOrderingApp, User, Admin

def main():
    app = FoodOrderingApp()

    while True:
        print("Welcome to the Food Ordering App")
        print("1. Admin Login")
        print("2. Admin Register")
        print("3. User Register")
        print("4. User Login")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")
            authenticated_admin = app.admin.login(admin_username, admin_password)
            if authenticated_admin:
                admin_menu(app)
            else:
                print("Admin authentication failed.")

        elif choice == "2":
            full_name = input("Enter your full name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            password = input("Enter your password: ")
            app.admin.register(full_name, phone_number, email, address, password)

        elif choice == "3":
            full_name = input("Enter your full name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            password = input("Enter your password: ")
            app.user.register(full_name, phone_number, email, address, password)

        elif choice == "4":
            user_email = input("Enter your email: ")
            user_password = input("Enter your password: ")
            authenticated_user = app.user.login(user_email, user_password)
            if authenticated_user:
                user_menu(app)
            else:
                print("User authentication failed.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu(app):
    while True:
        print("Admin Menu:")
        print("1. Add new food item")
        print("2. Edit food item")
        print("3. View food menu")
        print("4. Remove food item")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            app.admin.add_food_item()
        elif choice == "2":
            app.admin.edit_food_item()
        elif choice == "3":
            app.admin.view_food_menu()
        elif choice == "4":
            app.admin.remove_food_item()
        elif choice == "5":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(app):
    while True:
        print("User Menu:")
        print("1. Place New Order")
        print("2. Order History")
        print("3. Update Profile")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            app.user.place_order()
        elif choice == "2":
            app.user.view_order_history()
        elif choice == "3":
            app.user.update_profile()
        elif choice == "4":
            print("User logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.is_authenticated = False
        self.full_name = ""
        self.phone_number = ""
        self.email = ""
        self.address = ""
        self.password = ""
        self.orders = []

    def register(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.is_authenticated = True
        print("Admin registration successful.")

    def login(self, email, password):
        if email == self.email and password == self.password:
            self.is_authenticated = True
            print("Admin authentication successful.")
        else:
            print("Admin authentication failed. Please check your email and password.")

    def add_food_item(self, name, quantity, price, discount, stock):
        if not self.is_authenticated:
            print("Admin is not authenticated. Please log in.")
            return

        food_id = len(self.food_menu) + 1
        new_food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_menu.append(new_food_item)
        print(f"New food item '{name}' added to the menu with FoodID: {food_id}")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        if not self.is_authenticated:
            print("Admin is not authenticated. Please log in.")
            return

        for item in self.food_menu:
            if item.food_id == food_id:
                item.name = name
                item.quantity = quantity
                item.price = price
                item.discount = discount
                item.stock = stock
                print(f"Food item with FoodID {food_id} has been updated.")
                return
        print(f"Food item with FoodID {food_id} not found in the menu.")

    def view_food_menu(self):
        for item in self.food_menu:
            print(f"FoodID: {item.food_id}, Name: {item.name}, Quantity: {item.quantity}, Price: INR {item.price}, Discount: {item.discount}%, Stock: {item.stock}")

    def remove_food_item(self, food_id):
        if not self.is_authenticated:
            print("Admin is not authenticated. Please log in.")
            return

        for item in self.food_menu:
            if item.food_id == food_id:
                self.food_menu.remove(item)
                print(f"Food item with FoodID {food_id} has been removed from the menu.")
                return
        print(f"Food item with FoodID {food_id} not found in the menu.")

class User:
    def __init__(self):
        self.is_authenticated = False
        self.full_name = ""
        self.phone_number = ""
        self.email = ""
        self.address = ""
        self.password = ""
        self.orders = []

    def register(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.is_authenticated = True
        print("User registration successful.")

    def login(self, email, password):
        if email == self.email and password == self.password:
            self.is_authenticated = True
            print("User authentication successful.")
        else:
            print("User authentication failed. Please check your email and password.")

    def place_order(self, selected_items):
        if not self.is_authenticated:
            print("User is not authenticated. Please log in.")
            return

        total_price = 0
        for item in selected_items:
            print(f"Selected Item: {item.name} ({item.quantity}) [INR {item.price}]")
            total_price += item.price

        confirm = input(f"Total Price: INR {total_price}\nConfirm order (yes/no): ").strip().lower()
        if confirm == "yes":
            self.orders.append(selected_items)
            print("Order placed successfully.")
        else:
            print("Order canceled.")

    def view_order_history(self):
        if not self.is_authenticated:
            print("User is not authenticated. Please log in.")
            return

        if not self.orders:
            print("No order history found for this user.")
        else:
            print("Order History:")
            for i, order in enumerate(self.orders, start=1):
                print(f"Order {i}:")
                for item in order:
                    print(f"{item.name} ({item.quantity}) [INR {item.price}]")
                print(f"Total Price: INR {sum(item.price for item in order)}")

    def update_profile(self, full_name, phone_number, email, address, password):
        if not self.is_authenticated:
            print("User is not authenticated. Please log in.")
            return

        self.full_name = full_name if full_name else self.full_name
        self.phone_number = phone_number if phone_number else self.phone_number
        self.email = email if email else self.email
        self.address = address if address else self.address
        self.password = password if password else self.password
        print("User profile updated successfully.")

class FoodOrderingApp:
    def __init__(self):
        self.admin = Admin()
        self.users = []