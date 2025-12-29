from classes.community_driver import CommunityDriver
from classes.delivery_trip import DeliveryTrip
from classes.order import Order


def deliveryMenu():

    driver = CommunityDriver("D001", "Ahmad", "Van")
    trip = DeliveryTrip("T001")
    order1 = Order("O1001")
    order2 = Order("O1002")

    while True:

        print("\n===== Community Driver Delivery Menu =====")
        print("1. Assign Delivery Trip")
        print("2. Update Delivery Status")
        print("3. Add Order to Trip")
        print("4. View Trip Details")
        print("5. View Delivery Logs")
        print("6. Exit to Main Menu")

        choice = input("Select option: ")

        # Assign Trip
        if choice == "1":
            trip.assignDriver(driver)

        # Update Status
        elif choice == "2":
            newStatus = input("Enter new status (Assigned / On the Way / Delivered): ")
            trip.updateStatus(newStatus)

        # Aggregation 
        elif choice == "3":
            print("\nSelect order to add:")
            print("1. Order O1001")
            print("2. Order O1002")
            oc = input("Choose: ")

            if oc == "1":
                trip.addOrder(order1)
            else:
                trip.addOrder(order2)

        # Encapsulation 
        elif choice == "4":
            trip.viewTripDetails()

        # Traceability 
        elif choice == "5":
            trip.viewLogs()

        elif choice == "6":
            print("Returning to User Menu...")
            break

        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")

    