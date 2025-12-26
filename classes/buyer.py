from classes.user import User


class Buyer(User):
    def __init__(self, user_id, user_name, user_email,
                 delivery_address, payment_method):
        super().__init__(user_id, user_name, user_email)
        self.order_history = []
        self.delivery_address = delivery_address
        self.payment_method = payment_method

    def browse_produce(self):
        print("\nAvailable Produce:")
        print("1. Tomato - RM3/kg")
        print("2. Spinach - RM2/bunch")
        print("3. Corn - RM1.50/unit")

    def place_order(self):
        print("Order placed successfully.")
        self.order_history.append("Order #001")

    def view_orders(self):
        if not self.order_history:
            print("No orders yet.")
        else:
            print("Order History:")
            for order in self.order_history:
                print(order)