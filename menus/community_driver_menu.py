def communityDriverMenu(drivers, trips):
    while True:
        print("\n===== Community Driver Menu =====")
        print("1. Assign Trip")
        print("2. Update Status")
        print("3. Set Availability")
        print("4. Check Availability")
        print("5. Add Trip")
        print("6. Display Info")
        print("7. Back to Main Menu")
        
        choice = input("Select: ").strip()
        driverID = input("Enter Driver ID: ").strip()
        if driverID not in drivers:
            print("Driver not found.")
            continue
        driver = drivers[driverID]
        
        if choice == "1":
            tripID = input("Enter Trip ID: ").strip()
            if tripID in trips:
                driver.assignTrip(trips[tripID])
            else:
                print("Trip not found.")
        elif choice == "2":
            status = input("Enter status: ").strip()
            driver.updateStatus(status)
        elif choice == "3":
            avail = input("Available (y/n): ").strip().lower() == "y"
            driver.setAvailability(avail)
        elif choice == "4":
            print(f"Available: {driver.isAvailable()}")
        elif choice == "5":
            tripID = input("Enter Trip ID: ").strip()
            if tripID in trips:
                driver.addTrip(trips[tripID])
            else:
                print("Trip not found.")
        elif choice == "6":
            driver.displayInfo()
        elif choice == "7":
            break
        else:
            print("Invalid.")
        
        input("Press Enter...")