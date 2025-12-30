from classes.delivery_trip import deliveryTrip


def deliveryTripMenu(trips, drivers, orders):
    while True:
        print("\n===================================")
        print("          DELIVERY TRIP MENU       ")
        print("===================================")
        print("1. Assign Driver")
        print("2. Add Order to Trip")
        print("3. Update Trip Status")
        print("4. Calculate Cost")
        print("5. View Trip Details")
        print("6. Back to Main Menu")
        print("===================================")

        choice = input("Select option: ").strip()

        if choice == "6":
            print(f"Returning to Main Menu...")
            break

        trip_id = input("\nEnter Trip ID: ").strip()

        if trip_id not in trips:
            print("\nTrip not found.")
            continue

        trip = trips[trip_id]

        # ----- Menu Actions -----
        if choice == "1":
            driver_id = input("Enter Driver ID: ").strip()
            if driver_id in drivers:
                trip.assign_driver(drivers[driver_id])
            else:
                print("\nDriver not found.")

        elif choice == "2":
            order_id = input("Enter Order ID: ").strip()
            if order_id in orders:
                trip.add_order(order_id)
            else:
                print("\nOrder not found.")

        elif choice == "3":
            status = input("Enter new trip status: ")
            trip.update_status(status, "Village Coordinator")

        elif choice == "4":
            distance = float(input("Distance (km): "))
            weight = float(input("Total Weight (kg): "))
            cost = trip.calculate_cost(distance, weight)
            print(f"\nTrip Delivery Cost = RM{cost}")

        elif choice == "5":
            trip.view_trip_details()

        else:
            print("Invalid option. Please try again.")


