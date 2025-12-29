class communityDriver:
    def __init__(self, driver_id, name, vehicle_type, contact_number):
        self.driver_id = driver_id
        self.name = name
        self.vehicle_type = vehicle_type
        self.contact_number = contact_number
        self.availability = True
        self.rating = 5.0
        self.assigned_trips = []

    # ---------- Trip Assignment ----------
    def assign_trip(self, trip):
        self.assigned_trips.append(trip)
        self.availability = False
        print(f"Trip {trip.trip_id} assigned to {self.driver_id}")

    def add_trip(self, trip):
        self.assign_trip(trip)

    # ---------- Status Update ----------
    def update_delivery_status(self, trip, status, user="Driver"):
        trip.update_status(status, user)

    # ---------- Availability ----------
    def set_availability(self, value):
        self.availability = value
        print("Driver availability updated.")

    def is_available(self):
        return self.availability

    # ---------- Display ----------
    def display_info(self):
        print("\n===== DRIVER INFO =====")
        print(f"Driver ID: {self.driver_id}")
        print(f"Name: {self.name}")
        print(f"Vehicle: {self.vehicle_type}")
        print(f"Contact: {self.contact_number}")
        print(f"Available: {self.availability}")
        print(f"Assigned Trips: {len(self.assigned_trips)}")

