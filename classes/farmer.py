from classes.user import User

class Farmer(User):
    def __init__(self, user_id, user_name, user_email, farmName, farmLocation):
        super().__init__(user_id, user_name, user_email)
        self.__farmName = farmName
        self.__farmLocation = farmLocation
        self.__produceList = []

    def supplyProduce(self, produce):
        self.__produceList.append(produce)
        print(f"Produce supplied by farmer {self.__farmName}")

    def updateProduceDetails(self, produceID, weight=None, grade=None):
        for produce in self.__produceList:
            details = produce.getProduceDetails()
            if details["id"] == produceID:
                if weight is not None:
                    produce.updateWeight(weight)
                if grade is not None:
                    produce.updateGrade(grade)
                return
        print("Produce not found.")

    def viewSettlementStatement(self):
        print("\n===== Settlement Statement =====")
        print("Total Deliveries : Calculated by system")
        print("Net Payout       : RM XXX.XX")
        print("================================")

    def reviewDeliveryRecords(self):
        print("\nViewing delivery records...")