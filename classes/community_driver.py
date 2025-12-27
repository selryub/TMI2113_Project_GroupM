class CommunityDriver:
    def __init__(self, driverID, name, vehicleType):
        self.__driverID = driverID
        self.__name = name
        self.__vehicleType = vehicleType
        self.__availabilityStatus = True
        self.__assignedTrips = []

    def getName(self):
        return self.__name

    def isAvailable(self):
        return self.__availabilityStatus

    def setAvailability(self, status):
        self.__availabilityStatus = status
        print(f"Driver availability updated → {status}")

    # polymorphic behaviour when trip status changes
    def updateStatus(self, status):
        print(f"(Driver Notification) {self.__name} acknowledges status → {status}")

    # UC5 — assign trip to driver
    def assignTrip(self, trip):
        if not self.__availabilityStatus:
            print("Driver is currently unavailable.")
            return

        self.__assignedTrips.append(trip)
        self.__availabilityStatus = False
        print(f"Trip {trip.getTripID()} assigned to driver {self.__name}")
