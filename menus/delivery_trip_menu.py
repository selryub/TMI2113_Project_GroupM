def deliveryTripMenu(trips, drivers, orders):
    while True:
        print("\n===== Delivery Trip Menu =====")
        print("1. Assign Driver")
        print("2. Add Order")
        print("3. Update Status")
        print("4. View Trip Details")
        print("5. View Logs")
        print("6. Calculate Cost")
        print("7. Back to Main Menu")
        
        choice = input("Select: ").strip()
        tripID = input("Enter Trip ID: ").strip()
        if tripID not in trips:
            print("Trip not found.")
            continue
        trip = trips[tripID]
        
        if choice == "1":
            driverID = input("Enter Driver ID: ").strip()
            if driverID in drivers:
                trip.assignDriver(drivers[driverID])
            else:
                print("Driver not found.")
        elif choice == "2":
            orderID = input("Enter Order ID: ").strip()
            if orderID in orders:
                trip.addOrder(orders[orderID])
            else:
                print("Order not found.")
        elif choice == "3":
            status = input("Enter status: ").strip()
            trip.updateStatus(status)
        elif choice == "4":
            trip.viewTripDetails()
        elif choice == "5":
            trip.viewLogs()
        elif choice == "6":
            distance = float(input("Distance: ") or 10)
            weight = float(input("Weight: ") or 50)
            cost = trip.calculateCost(distance, weight)
            print(f"Cost: RM{cost}")
        elif choice == "7":
            break
        else:
            print("Invalid.")
        
        input("Press Enter...")