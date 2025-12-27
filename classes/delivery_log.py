class DeliveryLog:
    def __init__(self, logID, tripID, action, details, timestamp):
        self.__logID = logID
        self.__tripID = tripID
        self.__action = action
        self.__details = details
        self.__timestamp = timestamp

    # returns formatted string (for readability)
    def formatLog(self):
        return f"[Log {self.__logID}] ({self.__timestamp}) {self.__action} - {self.__details}"

    # prints output to screen (for UI test evidence)
    def displayLog(self):
        print("\n---------------- Delivery Log Entry ----------------")
        print(f"Log ID   : {self.__logID}")
        print(f"Trip ID  : {self.__tripID}")
        print(f"Action   : {self.__action}")
        print(f"Details  : {self.__details}")
        print(f"Time     : {self.__timestamp}")
        print("---------------------------------------------------")