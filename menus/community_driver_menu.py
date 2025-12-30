from classes.community_driver import communityDriver


def communityDriverMenu(drivers, trips):
    while True:
        print("\n===================================")
        print("        COMMUNITY DRIVER MENU      ")
        print("===================================")
        print("1. Assign Trip")
        print("2. Update Delivery Status")
        print("3. Set Availability")
        print("4. Check Availability")
        print("5. Display Driver Info")
        print("6. Back to Main Menu")
        print("===================================")

        choice = input("Select option: ").strip()

        if choice == "6":
            print(f"\nReturning to Main Menu...")
            break

        driver_id = input("\nEnter Driver ID: ").strip()

        if driver_id not in drivers:
            print("\nDriver not found.")
            continue

        driver = drivers[driver_id]

        # ----- Menu Options -----
        if choice == "1":
            trip_id = input("Enter Trip ID: ").strip()
            if trip_id in trips:
                driver.assign_trip(trips[trip_id])
            else:
                print("\nTrip not found.")

        elif choice == "2":
            trip_id = input("Enter Trip ID: ").strip()
            if trip_id in trips:
                status = input("Enter new delivery status: ").strip()
                driver.update_delivery_status(trips[trip_id], status, "Driver")
            else:
                print("\nTrip not found.")

        elif choice == "3":
            value = input("Available? (y/n): ").lower() == "y"
            driver.set_availability(value)

        elif choice == "4":
            print("\nDriver Availability Status:")
            print("---------------------------")
            print(f"{driver.isAvailable()}")

        elif choice == "5":
            driver.display_info()

        else:
            print("Invalid option. Please try again.")

