from classes.village_coordinator import VillageCoordinator
from classes.produce import Produce
from classes.farmer import Farmer
from classes.order import Order

def villageCoordinatorMenu():
    vc = VillageCoordinator(
        user_id=1,
        user_name="Alice",
        user_email="alice@gmail.com", 
        user_password="password123", 
        villageName="Happy Village", 
        contactNumber="0123456789"
    )

    tomato = Produce("P001", "Tomatoes", "Vegetables", "A", 100, 3.50)
    sample_farmer = Farmer(101, "John Doe", "john@gmail.com", "farm123", "Sunny Farm", "Kuching")

    order1 = Order("ORD001", "BUY001", "P001")
    order1.setQuantity(10)
    order1.calculateTotal(3.50)

    order2 = Order("ORD002", "BUY002", "P002")
    order2.setQuantity(5)
    order2.calculateTotal(2.50)

    vc.add_order_for_verification(order1)
    vc.add_order_for_verification(order2)

    vc.manageFarmer(sample_farmer)

    while True:
        print("\n===== VILLAGE COORDINATOR MENU =====")
        print("1. Verify Order")
        print("2. Approve Order")
        print("3. Reject Order")
        print("4. Record Produce Details")
        print("5. Schedule Delivery Trip")
        print("6. Manage Farmer")
        print("7. View Pending Orders")
        print("8. View Profile")
        print("0. Back to Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            order_id = input("Enter Order ID to verify: ")
            vc.verifyOrder(order_id)

        elif choice == "2":
            order_id = input("Enter Order ID to approve: ")
            vc.approveOrder(order_id)

        elif choice == "3":
            order_id = input("Enter Order ID to reject: ")
            reason = input("Enter rejection reason: ")
            vc.rejectOrder(order_id, reason)

        elif choice == "4":
            pid = input("Produce ID: ")
            pname = input("Produce Name: ")
            category = input("Category: ")
            grade = input("Grade: ")
            weight = float(input("Weight (kg): "))
            price = float(input("Price per kg: "))

            produce = Produce(pid, pname, category, grade, weight, price)
            vc.recordProduceDetails(produce, weight, grade, price)

        elif choice == "5":
            print("Scheduling Delivery Trip")

        elif choice == "6":
            fname = input("Farmer Name: ")
            femail = input("Farmer Email: ")

            new_farmer = Farmer(102, fname, femail, "temp123", fname + " Farm", "Local")
            vc.manageFarmer(new_farmer)

        elif choice == "7":
            vc.viewPendingOrders()

        elif choice == "8":
            vc.viewProfile()  # Polymorphism - Override

        elif choice == "0":
            break

        else:
            print("Invalid option.")