from classes.user import User

class Buyer(User):

    def __init__(self, user_id, user_name, user_email, delivery_address, payment_method):
        super().__init__(user_id, user_name, user_email)
        self.delivery_address = delivery_address
        self.payment_method = payment_method
        self.order_history = []

    def browse_produce(self):
        print("\nAvailable produce:")
        print("1. Tomato - RM3/kg")
        print("2. Spinach - RM2/bunch")
        print("3. Corn - RM1.50/unit")

    def place_order(self):
        produce = {
            1: ("Tomato", 3.00),
            2: ("Spinach", 2.00),
            3: ("Corn", 1.50)
        }

        print("\nAvailable Produce:")
        for key, value in produce.items():
            print(f"{key}. {value[0]} - RM{value[1]}")

        try:
            choice = int(input("Select produce number: "))
            quantity = int(input("Enter quantity: "))

            if choice in produce:
                item, price = produce[choice]
                total = price * quantity

                order = {
                    "item": item,
                    "quantity": quantity,
                    "total": total
                }

                self.order_history.append(order)

                print(f"\nOrder placed: {quantity} x {item}")
                print(f"Total price: RM{total:.2f}")
            else:
                print("Invalid selection.")

        except ValueError:
            print("Please enter valid numbers.")

    def view_orders(self):
        if not self.order_history:
            print("\nNo orders placed yet.")
            return

        print("\nOrder History:")
        for i, order in enumerate(self.order_history, start=1):
            print(
                f"{i}. {order['quantity']} x {order['item']} "
                f"(Total: RM{order['total']:.2f})"
            )