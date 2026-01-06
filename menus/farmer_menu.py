from classes.farmer import Farmer
from classes.produce import Produce

def farmerMenu():
    # Create a sample farmer object
    farmer = Farmer(
        user_id=1, 
        user_name="John Doe", 
        user_email="john@email.com", 
        user_password="password123", 
        farm_name="Sunny Farm", 
        farm_location="Kuching"
    )

    tomato = Produce("P001", "Tomatoes", "Vegetables", "A", 100, 3.50)
    spinach = Produce("P002", "Spinach", "Leafy Greens", "B", 50, 2.80)
    farmer.supply_produce(tomato)
    farmer.supply_produce(spinach)
    farmer.deliver_produce("P001", 20, "ORD001")
    farmer.deliver_produce("P002", 15, "ORD002")

    while True:
        print("\n===== FARMER MENU =====")
        print("1. Supply Produce")
        print("2. Update Produce Details")
        print("3. Deliver Produce")
        print("4. View Settlement Statement")
        print("5. Review Delivery Records")
        print("6. View Profile")
        print("0. Back to Main Menu")

        choice = input("Select option: ").strip()

        if choice == "1":
            pid = input("Produce ID: ")
            pname = input("Produce Name: ")
            category = input("Category: ")
            grade = input("Grade: ")
            weight = float(input("Weight (kg): "))
            price = float(input("Price per kg: "))
            produce = Produce(pid, pname, category, grade, weight, price)
            farmer.supply_produce(produce)

        elif choice == "2":
            pid = input("Enter Produce ID to update: ")
            weight = input("Enter new weight (leave blank to skip): ")
            grade = input("Enter new grade (leave blank to skip): ")
            price_input = input("Enter new price (leave blank to skip): ")
            
            weight_val = float(weight) if weight else None
            grade_val = grade if grade else None
            price_val = float(price_input) if price_input else None

            farmer.update_produce_details(pid, weight=weight_val, grade=grade_val, price=price_val)

        elif choice == "3":
            pid = input("Enter Produce ID to deliver: ")
            quantity = float(input("Enter quantity to deliver (kg): "))
            order_id = input("Enter Order ID (optional, press Enter to skip): ")

            if order_id == "":
                order_id = None
            
            farmer.deliver_produce(pid, quantity, order_id)

        elif choice == "4":
            farmer.view_settlement_statement()

        elif choice == "5":
            farmer.review_delivery_records()

        elif choice == "6":
            farmer.view_profile()  # Polymorphism - Override

        elif choice == "0":
            break

        else:
            print("Invalid option.")
