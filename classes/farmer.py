from classes.user import User

class Farmer(User):
    def __init__(self, user_id, user_name, user_email, user_password, farm_name, farm_location):
        super().__init__(user_id, user_name, user_email, user_password)
        self.__farm_name = farm_name
        self.__farm_location = farm_location
        self.__produce_list = []  # renamed for PEP8

    # Polymorphism - Method Override from User class
    def view_profile(self):
        print("\n===== FARMER PROFILE =====")
        print(f"User ID   : {self.userID}")
        print(f"Name      : {self.userName}")
        print(f"Email     : {self.userEmail}")
        print(f"Farm Name : {self.__farm_name}")
        print(f"Location  : {self.__farm_location}")
        print(f"Produce   : {len(self.__produce_list)} items")
        print("==========================")

    def supply_produce(self, produce):
        self.__produce_list.append(produce)
        print(f"Produce supplied by farmer {self.__farm_name}")

    def update_produce_details(self, produce_id, weight=None, grade=None):
        for produce in self.__produce_list:
            details = produce.getProduceDetails()
            if details["id"] == produce_id:
                if weight is not None:
                    produce.updateWeight(weight)
                if grade is not None:
                    produce.updateGrade(grade)
                print(f"Produce {produce_id} updated successfully.")
                return
        print("Produce not found.")

    def view_settlement_statement(self):
        total_deliveries = len(self.__produce_list)
        net_payout = sum(
            produce.getProduceDetails()["weight"] * produce.getProduceDetails()["price"]
            for produce in self.__produce_list
        )

        print("\n===== Settlement Statement =====")
        print(f"Total Deliveries : {total_deliveries} items")
        print(f"Net Payout       : RM {net_payout:.2f}")
        print("================================")

    def review_delivery_records(self):
        if not self.__produce_list:
            print("\nNo delivery records found.")
            return

        print("\n===== Delivery Records =====")
        for produce in self.__produce_list:
            details = produce.getProduceDetails()
            print(f"ID: {details['id']}, Name: {details['name']}, "
                  f"Category: {details['category']}, Grade: {details['grade']}, "
                  f"Weight: {details['weight']} kg, Price/kg: RM {details['price']:.2f}")
        print("============================")
