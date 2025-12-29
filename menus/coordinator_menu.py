from classes.village_coordinator import VillageCoordinator
from classes.produce import Produce

def villageCoordinatorMenu():
    vc = VillageCoordinator(1, "Alice", "alice@email.com", "Happy Village", "012-3456789")

    while True:
        print("\n===== VILLAGE COORDINATOR MENU =====")
        print("1. Verify Order (stub)")
        print("2. Approve Order (stub)")
        print("3. Reject Order (stub)")
        print("4. Record Produce Details")
        print("5. Schedule Delivery Trip (stub)")
        print("6. Manage Farmer")
        print("7. View Pending Orders")
        print("0. Back to Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            print("Verifying Order (functionality to be implemented)")

        elif choice == "2":
            print("Approving Order (functionality to be implemented)")

        elif choice == "3":
            print("Rejecting Order (functionality to be implemented)")

        elif choice == "4":
            pid = input("Produce ID: ")
            pname = input("Produce Name: ")
            category = input("Category: ")
            grade = input("Grade: ")
            weight = float(input("Weight (kg): "))
            price = float(input("Price per kg: "))
            produce = Produce(pid, pname, category, grade, weight, price)
            vc.recordProduceDetails(produce, weight, grade)

        elif choice == "5":
            print("Scheduling Delivery Trip (functionality to be implemented)")

        elif choice == "6":
            fname = input("Farmer Name: ")
            f = input("Farmer Email: ")
            farmer = f  # stub: you could create Farmer instance if needed
            vc.manageFarmer(fname)

        elif choice == "7":
            vc.viewPendingOrders()

        elif choice == "0":
            break

        else:
            print("Invalid option.")