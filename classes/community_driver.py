class communityDriver:
    def __init__(self, driver_id, name, vehicle_type, contact_number):
        self.driver_id = driver_id
        self.name = name
        self.vehicle_type = vehicle_type
        self.contact_number = contact_number
        self.__availability = True
        self.rating = 5.0
        self.assigned_trips = []

    # ---------- Assign Trip ----------
    def assign_trip(self, trip):
        self.assigned_trips.append(trip)
        self.__availability = False
        print(f"Trip {trip.trip_id} assigned to {self.driver_id}")

    def add_trip(self, trip):
        self.assign_trip(trip)

    # ---------- Status Update ----------
    def update_delivery_status(self, trip, status, user="Driver"):
        if trip in self.assigned_trips:
            trip.status = status
            print(f"Trip {trip.trip_id} status updated to {status}.")
        else:
            print(f"Error: Trip {trip.trip_id} is not assigned to driver {self.name}.")
       
    # ---------- Availability ----------
    def set_availability(self, value):
        self.__availability = value
        print("Driver availability updated.")

    def isAvailable(self):
        return "Available" if self.__availability else "Not Available"


    # ---------- Display ----------
    def display_info(self):
        print("\n===== DRIVER INFO =====")
        print(f"Driver ID: {self.driver_id}")
        print(f"Name: {self.name}")
        print(f"Vehicle: {self.vehicle_type}")
        print(f"Contact: {self.contact_number}")
        print(f"Available: {self.isAvailable()}")
        print(f"Assigned Trips: {len(self.assigned_trips)}")

        if not self.assigned_trips:
            print("No trips assigned yet.")
            return

        print("\n--- Assigned Trip Details ---")
        for trip in self.assigned_trips:
            print(f"Trip ID: {trip.trip_id} | Status: {trip.status}")

