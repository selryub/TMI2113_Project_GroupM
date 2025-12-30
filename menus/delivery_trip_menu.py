from classes.delivery_trip import deliveryTrip


def deliveryTripMenu(trips, drivers, orders):
    while True:
        print("\n===== DELIVERY TRIP MENU =====")
        print("1. Assign Driver")
        print("2. Add Order to Trip")
        print("3. Update Trip Status")
        print("4. Calculate Cost")
        print("5. View Trip Details")
        print("6. View Trip Logs")
        print("7. Back to Main Menu")

        choice = input("Select: ").strip()

        if choice == "7":
            break

        trip_id = input("Enter Trip ID: ").strip()

        if trip_id not in trips:
            print("Trip not found.")
            continue

        trip = trips[trip_id]

        # ----- Menu Actions -----
        if choice == "1":
            driver_id = input("Enter Driver ID: ").strip()
            if driver_id in drivers:
                trip.assign_driver(drivers[driver_id])
            else:
                print("Driver not found.")

        elif choice == "2":
            order_id = input("Enter Order ID: ").strip()
            if order_id in orders:
                trip.add_order(order_id)
            else:
                print("Order not found.")

        elif choice == "3":
            status = input("Enter new status: ")
            trip.update_status(status, "Village Coordinator")

        elif choice == "4":
            distance = float(input("Distance (km): "))
            weight = float(input("Total Weight (kg): "))
            cost = trip.calculate_cost(distance, weight)
            print(f"Trip Cost = RM{cost}")

        elif choice == "5":
            trip.view_trip_details()

        elif choice == "6":
            trip.view_logs()

        else:
            print("Invalid option.")


