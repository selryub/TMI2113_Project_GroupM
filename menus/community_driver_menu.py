from classes.community_driver import communityDriver


def communityDriverMenu(drivers, trips):
    while True:
        print("\n===== COMMUNITY DRIVER MENU =====")
        print("1. Assign Trip")
        print("2. Update Delivery Status")
        print("3. Set Availability")
        print("4. Check Availability")
        print("5. Display Driver Info")
        print("6. Back to Main Menu")

        choice = input("Select: ").strip()

        if choice == "6":
            break

        driver_id = input("Enter Driver ID: ").strip()

        if driver_id not in drivers:
            print("Driver not found.")
            continue

        driver = drivers[driver_id]

        # ----- Menu Options -----
        if choice == "1":
            trip_id = input("Enter Trip ID: ").strip()
            if trip_id in trips:
                driver.assign_trip(trips[trip_id])
            else:
                print("Trip not found.")

        elif choice == "2":
            trip_id = input("Enter Trip ID: ").strip()
            if trip_id in trips:
                status = input("Enter new status: ")
                driver.update_delivery_status(trips[trip_id], status, "Driver")
            else:
                print("Trip not found.")

        elif choice == "3":
            value = input("Set available? (y/n): ").lower() == "y"
            driver.set_availability(value)

        elif choice == "4":
            print(f"Available: {driver.isAvailable()}")

        elif choice == "5":
            driver.display_info()

        else:
            print("Invalid option.")

        input("Press Enter to continue...")
