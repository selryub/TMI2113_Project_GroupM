from classes.delivery_log import deliveryLog


class deliveryTrip:
    def __init__(self, trip_id, distance_km=0):
        self.trip_id = trip_id
        self.assigned_driver = None
        self.status = "Pending"
        self.orders = []
        self.distance_km = distance_km
        self.estimated_time = 0
        self.cost = 0
        self.log = deliveryLog(trip_id)

        self.log.add_entry("Trip created")

    # ---------- Association with Driver ----------
    def assign_driver(self, driver):
        self.assigned_driver = driver
        driver.assign_trip(self)
        self.log.add_entry(f"Driver assigned: {driver.driver_id}")

    # ---------- Aggregation with Orders ----------
    def add_order(self, order):
        self.orders.append(order)
        self.log.add_entry(f"Order added: {order}")

    # ---------- Status Update ----------
    def update_status(self, new_status, user="System"):
        self.status = new_status
        self.log.add_entry(f"Trip status updated to {new_status}", user)

    # ---------- Cost Calculation ----------
    def calculate_cost(self, distance_km, total_weight):
        self.distance_km = distance_km
        self.cost = round((distance_km * 1.5) + (total_weight * 0.5), 2)
        self.log.add_entry(f"Cost recalculated: RM{self.cost}")
        return self.cost

    # ---------- Reporting ----------
    def view_trip_details(self):
        print("\n===== TRIP DETAILS =====")
        print(f"Trip ID: {self.trip_id}")
        print(f"Driver: {self.assigned_driver.driver_id if self.assigned_driver else 'Unassigned'}")
        print(f"Status: {self.status}")
        print(f"Orders in Trip: {len(self.orders)}")
        print(f"Distance: {self.distance_km} km")
        print(f"Estimated Time: {self.estimated_time} mins")
        print(f"Cost: RM{self.cost}")

    def view_logs(self):
        self.log.display_log()

