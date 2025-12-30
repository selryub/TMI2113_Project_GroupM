from classes.user import User

class VillageCoordinator(User):
    def __init__(self, user_id, user_name, user_email, user_password, villageName, contactNumber):
        super().__init__(user_id, user_name, user_email, user_password)
        self.__villageName = villageName
        self.__contactNumber = contactNumber
        self.__managedFarmers = []

    # Polymorphism - Method Override from User class
    def viewProfile(self):
        print("\n===== COORDINATOR PROFILE =====")
        print(f"User ID    : {self.userID}")
        print(f"Name       : {self.userName}")
        print(f"Email      : {self.userEmail}")
        print(f"Village    : {self.__villageName}")
        print(f"Contact    : {self.__contactNumber}")
        print(f"Farmers    : {len(self.__managedFarmers)} managed")
        print("===============================")

    # UC4 — Verify Orders
    def verifyOrder(self, order):
        print(f"Verifying Order {order.getOrderID()}...")
        order.updateStatus("Verified")

    def approveOrder(self, order):
        order.updateStatus("Approved")
        print(f"Order {order.getOrderID()} approved")

    def rejectOrder(self, order):
        order.updateStatus("Rejected")
        print(f"Order {order.getOrderID()} rejected")

    # UC5 — Record Produce Details
    def recordProduceDetails(self, produce, weight, grade):
        produce.updateWeight(weight)
        produce.updateGrade(grade)
        print("Produce details recorded by Village Coordinator")

    # UC6 — Assign Delivery Trip
    def scheduleDeliveryTrip(self, trip, driver):
        trip.assign_driver(driver)
        print("Delivery trip scheduled")

    def manageFarmer(self, farmer):
        self.__managedFarmers.append(farmer)
        print(f"Farmer {farmer} assigned to coordinator")

    def viewPendingOrders(self):
        print("Displaying pending orders...")