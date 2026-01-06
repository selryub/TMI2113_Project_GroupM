from classes.user import User
from classes.order import Order

class VillageCoordinator(User):
    def __init__(self, user_id, user_name, user_email, user_password, villageName, contactNumber):
        super().__init__(user_id, user_name, user_email, user_password)
        self.__villageName = villageName
        self.__contactNumber = contactNumber
        self.__managedFarmers = []
        self.__pending_orders = []
        self.__verified_orders = []

    # Polymorphism - Method Override from User class
    def viewProfile(self):
        print("\n===== COORDINATOR PROFILE =====")
        print(f"User ID    : {self.userID}")
        print(f"Name       : {self.userName}")
        print(f"Email      : {self.userEmail}")
        print(f"Village    : {self.__villageName}")
        print(f"Contact    : {self.__contactNumber}")
        print(f"Farmers    : {len(self.__managedFarmers)} managed")
        print(f"Pending    : {len(self.__pending_orders)} orders")
        print(f"Verified   : {len(self.__verified_orders)} orders")
        print("===============================")

    def add_order_for_verification(self, order):
        self.__pending_orders.append(order)
        print(f"Order {order.getOrderID()} added for verification")

    # UC4 — Verify Orders
    def verifyOrder(self, order_id):
        for order in self.__pending_orders:
            if order.getOrderID() == order_id:
                order.updateStatus("Verified", "Verified by Coordinator")
                self.__verified_orders.append(order)
                self.__pending_orders.remove(order)
                print(f"Order {order_id} verified successfully")
                return order
            
        print(f"Order {order_id} not found in pending list")
        return None

    def approveOrder(self, order_id):
        for order in self.__verified_orders:
            if order.getOrderID() == order_id:
                order.updateStatus("Approved", "Approved by Coordinator")
                print(f"Order {order_id} approved for delivery")
                return order
            
        print(f"Order {order_id} is not found in verified list")
        return None

    def rejectOrder(self, order_id, reason=""):
        for order in self.__pending_orders:
           if order.getOrderID() == order_id:
               order.updateStatus("Rejected", f"Rejected: {reason}")
               self.__pending_orders.remove(order)
               print(f"Order {order_id} rejected")
               return order
           
        print(f"Order {order_id} not found")
        return None

    # UC5 — Record Produce Details
    def recordProduceDetails(self, produce, weight=None, grade=None, price=None):
        if weight is not None:
            produce.updateWeight(weight)
        if grade is not None:
            produce.updateGrade(grade)
        if price is not None:
            produce.updatePrice(price)

        print("Produce details recorded by Village Coordinator")
        return produce

    # UC6 — Assign Delivery Trip
    def scheduleDeliveryTrip(self, trip, driver):
        trip.assign_driver(driver)
        print("Delivery trip scheduled")
        return True

    def manageFarmer(self, farmer):
        self.__managedFarmers.append(farmer)
        print(f"Farmer assigned to coordinator")

    def viewPendingOrders(self):
        if not self.__pending_orders:
            print("\nNo pending orders")
            return
        
        print("\n===== PENDING ORDERS =====")
        for order in self.__pending_orders:
            print(f"Order ID: {order.getOrderID()}")
            print(f"Buyer ID: {order.getBuyerID()}")
            print(f"Produce ID: {order.getProduceID()}")
            print(f"Quantity: {order.getQuantity()}")
            print(f"Total: RM{order.getTotalPrice():.2f}")
            print(f"Status: {order.getStatus()}")
            print("-" * 30)
        print("===========================")