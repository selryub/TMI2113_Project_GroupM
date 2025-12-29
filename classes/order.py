class Order:
    def __init__(self, orderID, buyerID, produceID):
        self.__orderID = orderID
        self.__buyerID = buyerID
        self.__produceID = produceID
        self.__quantity = 0
        self.__totalPrice = 0.0
        self.__status = "Pending"
        self.__notes = ""

    # Getter methods
    def getOrderID(self):
        return self.__orderID

    def getBuyerID(self):
        return self.__buyerID

    def getProduceID(self):
        return self.__produceID

    def getQuantity(self):
        return self.__quantity

    def getTotalPrice(self):
        return self.__totalPrice

    def getStatus(self):
        return self.__status

    # Setter methods
    def setQuantity(self, quantity):
        self.__quantity = quantity
        print(f"Quantity set to {quantity}")

    # Polymorphism - Method Overloading (using default parameter)
    def calculateTotal(self, price):
        self.__totalPrice = price * self.__quantity
        print(f"Total calculated: RM{self.__totalPrice:.2f}")

    # Polymorphism - Method Overloading (different parameters)
    def calculateTotalWithDiscount(self, price, quantity, discount):
        self.__quantity = quantity
        discountAmount = (price * quantity) * (discount / 100)
        self.__totalPrice = (price * quantity) - discountAmount
        print(f"Total with {discount}% discount: RM{self.__totalPrice:.2f}")

    # Polymorphism - Method Overloading (with optional notes)
    def updateStatus(self, newStatus, notes=""):
        self.__status = newStatus
        self.__notes = notes
        print(f"Order {self.__orderID} status updated to {newStatus}")
        if notes:
            print(f"Notes: {notes}")

    def viewOrderDetails(self):
        print("\n===== ORDER DETAILS =====")
        print(f"Order ID   : {self.__orderID}")
        print(f"Buyer ID   : {self.__buyerID}")
        print(f"Produce ID : {self.__produceID}")
        print(f"Quantity   : {self.__quantity}")
        print(f"Total Price: RM{self.__totalPrice:.2f}")
        print(f"Status     : {self.__status}")
        if self.__notes:
            print(f"Notes      : {self.__notes}")
        print("=========================")