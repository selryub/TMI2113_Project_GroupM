class DeliveryTrip:
    def __init__(self, tripID):
        self.__tripID = tripID
        self.__status = "Pending"
        self.__assignedDriver = None
        self.__orders = []
        self.__logs = []

    def assignDriver(self, driver):
        self.__assignedDriver = driver
        self.__status = "Assigned"
        self.__logs.append(f"Driver {driver.getName()} assigned to Trip {self.__tripID}")
        print(f"✔ Driver {driver.getName()} assigned to Trip {self.__tripID}")

    def addOrder(self, order):
        self.__orders.append(order)
        self.__logs.append(f"Order {order.getOrderID()} added to Trip {self.__tripID}")
        print(f"✔ Order {order.getOrderID()} added to Trip {self.__tripID}")

    def updateStatus(self, newStatus):
        self.__status = newStatus
        if self.__assignedDriver:
            self.__assignedDriver.updateStatus(newStatus)   # polymorphism call
        self.__logs.append(f"Trip {self.__tripID} updated to '{newStatus}' status")
        print(f"✔ Trip {self.__tripID} status updated to {newStatus}")

    def calculateCost(self, distance, weight):
        cost = (distance * 0.5) + (weight * 0.2)
        self.__logs.append(f"Cost calculated RM{cost}")
        print(f"✔ Delivery Cost = RM{cost}")
        return cost

    def viewTripDetails(self):
        driver = self.__assignedDriver.getName() if self.__assignedDriver else "None"
        print("\n🛈 Trip Details")
        print(f"Trip ID       : {self.__tripID}")
        print(f"Status        : {self.__status}")
        print(f"Driver        : {driver}")
        print(f"Orders Count  : {len(self.__orders)}")

    def viewLogs(self):
        print("\n📝 Delivery Logs:")
        for log in self.__logs:
            print(f"- {log}")

    def getTripID(self):
        return self.__tripID
