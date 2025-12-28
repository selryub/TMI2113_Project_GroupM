from datetime import datetime
from classes.delivery_log import DeliveryLog

class DeliveryTrip:
    def __init__(self, tripID):
        self.__tripID = tripID
        self.__status = "Pending"
        self.__assignedDriver = None
        self.__orders = []
        self.__logs = []

    def getTripID(self):
        return self.__tripID

    # UC5 — assign driver to trip
    def assignDriver(self, driver):
        self.__assignedDriver = driver
        driver.assignTrip(self)
        self.__status = "Assigned"

        log = DeliveryLog(
            logID=len(self.__logs) + 1,
            tripID=self.__tripID,
            action="Driver Assigned",
            details=f"{driver.getName()} assigned to trip",
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        self.__logs.append(log)
        print(f"✔ Driver {driver.getName()} successfully assigned to Trip {self.__tripID}")

    # aggregation — orders added into trip
    def addOrder(self, order):
        self.__orders.append(order)

        log = DeliveryLog(
            logID=len(self.__logs) + 1,
            tripID=self.__tripID,
            action="Order Added",
            details=f"Order {order.getOrderID()} added to trip",
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        self.__logs.append(log)
        print(f"✔ Order {order.getOrderID()} added into Trip {self.__tripID}")

    # UC6 — update delivery status
    def updateStatus(self, newStatus):
        self.__status = newStatus

        if self.__assignedDriver:
            self.__assignedDriver.updateStatus(newStatus)

        log = DeliveryLog(
            logID=len(self.__logs) + 1,
            tripID=self.__tripID,
            action="Status Updated",
            details=f"Trip status changed to {newStatus}",
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        self.__logs.append(log)
        print(f"✔ Trip {self.__tripID} status updated to {newStatus}")

    # used for UI testing / encapsulation evidence
    def viewTripDetails(self):
        driver = self.__assignedDriver.getName() if self.__assignedDriver else "None"

        print("\n=========== Trip Details ===========")
        print(f"Trip ID      : {self.__tripID}")
        print(f"Status       : {self.__status}")
        print(f"Driver       : {driver}")
        print(f"Orders Count : {len(self.__orders)}")
        print("====================================")

    def viewLogs(self):
        print("\n=========== Delivery Logs ==========")
        if len(self.__logs) == 0:
            print("No logs recorded yet.")
        else:
            for log in self.__logs:
                log.displayLog()
        print("====================================")

