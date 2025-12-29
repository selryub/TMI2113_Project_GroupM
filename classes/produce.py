class Produce:
    def __init__(self, produceID, produceName, category, grade, weight, pricePerKg):
        self.__produceID = produceID
        self.__produceName = produceName
        self.__category = category
        self.__grade = grade
        self.__weight = weight
        self.__pricePerKg = pricePerKg
        self.__availabilityStatus = True  

    def updateWeight(self, weight):
        self.__weight = weight
        print(f"Produce weight updated to {weight} kg")

    def updateGrade(self, grade):
        self.__grade = grade
        print(f"Produce grade updated to {grade}")

    def updatePrice(self, price):
        self.__pricePerKg = price
        print(f"Produce price updated to RM{price}/kg")

    def getProduceDetails(self):
        return {
            "id": self.__produceID,
            "name": self.__produceName,
            "category": self.__category,
            "grade": self.__grade,
            "weight": self.__weight,
            "price": self.__pricePerKg
        }

    def viewProduceDetails(self):
        details = self.getProduceDetails()
        return (f"ID: {details['id']}\n"
                f"Name: {details['name']}\n"
                f"Category: {details['category']}\n"
                f"Grade: {details['grade']}\n"
                f"Weight: {details['weight']} kg\n"
                f"Price: RM{details['price']}/kg\n"
                f"Availability: {'Available' if self.checkAvailability() else 'Not Available'}")

    def checkAvailability(self):
        return self.__availabilityStatus  

    def setAvailability(self, availability):
        self.__availabilityStatus = availability  
