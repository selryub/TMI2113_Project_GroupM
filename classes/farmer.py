from classes.user import User
from classes.produce import Produce

class Farmer(User):
    def __init__(self, user_id, user_name, user_email, user_password, farm_name, farm_location):
        super().__init__(user_id, user_name, user_email, user_password)
        self.__farm_name = farm_name
        self.__farm_location = farm_location
        self.__produce_list = []  # renamed for PEP8
        self.__delivery_records = []

    # Polymorphism - Method Override from User class
    def view_profile(self):
        print("\n===== FARMER PROFILE =====")
        print(f"User ID   : {self.userID}")
        print(f"Name      : {self.userName}")
        print(f"Email     : {self.userEmail}")
        print(f"Farm Name : {self.__farm_name}")
        print(f"Location  : {self.__farm_location}")
        print(f"Produce   : {len(self.__produce_list)} items")
        print(f"Deliveries: {len(self.__delivery_records)} records")
        print("==========================")

    def supply_produce(self, produce):
        self.__produce_list.append(produce)
        print(f"Inventory updated: {produce.getProduceDetails() ['name']}")
        return produce

    def update_produce_details(self, produce_id, weight=None, grade=None, price=None):
        for produce in self.__produce_list:
            details = produce.getProduceDetails()
            if details["id"] == produce_id:
                updates = []

                if weight is not None:
                    produce.updateWeight(weight)
                if grade is not None:
                    produce.updateGrade(grade)
                if price is not None:
                    produce.updatePrice(price)
                print(f"Produce {produce_id} updated successfully.")
                return True
        print("Produce not found.")
        return False

    def deliver_produce(self, produce_id, quantity, order_id=None):
        for produce in self.__produce_list:
            if produce.getProduceDetails()["id"] == produce_id:
                details = produce.getProduceDetails()

                self.__delivery_records.append({
                    'date': '2024-01-01',
                    'produce_id': produce_id,
                    'produce_name': details['name'],
                    'quantity': quantity,
                    'price_per_kg': details['price'],
                    'total': details['price'] * quantity,
                    'order_id': order_id or 'N/A'
                })

                print(f"Delivery recorded: {quantity}kg of {details['name']}")
                return True
            
        print(f"Produce {produce_id} not found")
        return False

    def view_settlement_statement(self):
        net_payout = sum(record['total'] for record in self.__delivery_records)
        total_deliveries = len(self.__delivery_records)

        print("\n===== Settlement Statement =====")
        print(f"Total Deliveries : {total_deliveries} records")
        print(f"Net Payout       : RM {net_payout:.2f}")
        print("================================")
        return net_payout

    def review_delivery_records(self):
        if not self.__delivery_records:
            print("\nNo delivery records found.")
            return

        print("\n===== Delivery Records =====")
        for i, record in enumerate(self.__delivery_records, 1):
            print(f"Record {i}:")
            print(f"Product : {record['produce_name']}")
            print(f"Quantity: {record['quantity']}kg")
            print(f"Price   : RM{record['price_per_kg']}/kg")
            print(f"Total   : RM{record['total']:.2f}")
            print(f"Order   : {record['order_id']}")
            print()
        print("============================")
