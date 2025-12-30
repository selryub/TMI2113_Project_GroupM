class deliveryTrip:
    def __init__(self, trip_id, distance=0):
        self.trip_id = trip_id
        self.assigned_driver = None
        self.status = "Pending"
        self.orders = []
        self.distance = distance
        self.estimated_time = 0
        self.cost = 0

        print(f"Trip created")

    # ---------- Association with Driver ----------
    def assign_driver(self, driver):
        self.assigned_driver = driver
        driver.assign_trip(self)

    # ---------- Aggregation with Orders ----------
    def add_order(self, order):
        if not self.assigned_driver:
            print(f"Error: Cannot add order. Assign a driver to Trip {self.trip_id} first.")
            return

        self.orders.append(order)
        print(f"Order added to Trip {self.trip_id}.")

    # ---------- Status Update ----------
    def update_status(self, new_status, user="System"):
        if not self.assigned_driver:
            print(f"Error: Cannot update status. Assign a driver to Trip {self.trip_id} first.")
            return

        self.status = new_status
        print(f"Trip {self.trip_id} status updated to {new_status} by {user}.")

    # ---------- Cost Calculation ----------
    def calculate_cost(self, distance, total_weight, average_speed = 40):

        if not self.assigned_driver:
            print(f"Error: Cannot calculate cost. Assign a driver to Trip {self.trip_id} first.")
            self.cost = 0
            self.estimated_time = 0
            return 0

        # Validation rules
        if distance <= 0:
            print(f"Error: Invalid distance value ({distance} km). Cost calculation terminated.")
            self.cost = 0
            self.estimated_time = 0
            return 0
        
        if total_weight < 0:
            print(f"Error: Invalid weight value ({total_weight} kg). Cost calculation terminated.")
            self.cost = 0
            self.estimated_time = 0
            return 0
        
        if average_speed <= 0:
            print(f"Error: Cost calculation failed due to invalid average speed value ({average_speed}).")
            self.cost = 0
            self.estimated_time = 0
            return 0
        
        # Store distance
        self.distance = distance 

        # Calculate delivery cost
        self.cost = round((distance * 1.5) + (total_weight * 0.5), 2)

        # Calculate estimated time
        if distance > 0 and average_speed > 0:

            # time (hours) = distance / speed
            # covert to minutes
            self.estimated_time = round((distance / average_speed) * 60)
        else:
            self.estimated_time = 0

        return self.cost

    # ---------- Reporting ----------
    def view_trip_details(self):
        print("\n===== TRIP DETAILS =====")
        print(f"Trip ID: {self.trip_id}")
        print(f"Driver: {self.assigned_driver.driver_id if self.assigned_driver else 'Unassigned'}")
        print(f"Status: {self.status}")
        print(f"Orders: {len(self.orders)}")
        print(f"Distance: {self.distance} km") 
        print(f"Estimated Time: {self.estimated_time} mins")
        print(f"Cost: RM{self.cost}")



